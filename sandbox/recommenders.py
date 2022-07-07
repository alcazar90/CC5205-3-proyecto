# Módulos
import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression
import os
import torch
import torchvision
from torch import nn
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torch.utils.data import Dataset

from sklearn.preprocessing import StandardScaler

import warnings
warnings.filterwarnings("ignore")

plt.style.use("bmh")

# Funciones

np.random.seed(1991)

def validar_lista(validation_playlists, validation_tracks, input_pid, input_track_uris, recomendador, n=20):
    input_df=validation_tracks.set_index("uri").loc[np.random.choice(input_track_uris, n)]
    output_uris= recomendador.recommend_list(input_df, number=len(input_track_uris)-n)
    output_pid= validation_playlists.set_index("track_uri").loc[output_uris]["pid"]
    return sum(output_pid==input_pid)*100.0/(len(input_track_uris)-n)

def validar_recomendador(validation_playlists, validation_tracks, pids, recomendador):
    total_playlists = len(pids)
    porcentajes=np.zeros(total_playlists)
    
    for i, pid in enumerate(pids):
        input_uris= list(set(validation_playlists[validation_playlists["pid"]==pid]["track_uri"]))
        porcentajes[i] = validar_lista(validation_playlists, validation_tracks, pid, input_uris, recomendador)
        if (i+1)%5==0:
            print(f"Generando recomendaciones Playlist {i + 1} de {total_playlists}. % Recomendaciones correctas: {round(porcentajes[i], 2)}")
    
    media_porc_rec = np.mean(porcentajes)
    plt.figure(figsize=(10, 5))
    plt.hist(porcentajes, bins=range(0, 101, 5), edgecolor='steelblue', color="deepskyblue")
    plt.axvline(media_porc_rec, color="midnightblue", label=f"% Recomendación promedio: {round(media_porc_rec, 2)}")
    plt.xticks(range(0, 101, 5))
    plt.title(f"Cantidad de % de canciones recomendados correctamente {type(recomendador).__name__}")
    plt.ylabel("Cantidad")
    plt.xlabel("% Recomendado correctamente")
    plt.legend()
    
    return media_porc_rec 

class Recommender1:
    def __init__(self, avg_features_by_pid_all):
        self.proximity_matrix=None
        self.obs_labels=None
        self.N_nearest=None
        self.artist=None
        self.pid_id=None
        self.avg_features_by_pid=None
        self.avg_features_by_pid_all=avg_features_by_pid_all
        
    def fit(self, X, y, artist):
        """Almacena la matriz de proximidad y guarda los PID en self.obs_labels"""
        self.avg_features_by_pid = X
        self.obs_labels = y
        self.proximity_matrix = distance_matrix(X, X)
        self.artist = artist
        
    def refit(self):
        """Actualiza la matriz de distancia en base a self.avg_features_by_pid"""
        self.proximity_matrix = distance_matrix(self.avg_features_by_pid, self.avg_features_by_pid)
        
    def recommend_list(self, canciones_df, number=2, N=50, **kwargs):
        """
           Recibe un set de canciones sin PID con sus track_features (canciones_df).
           Se recomputa self.proximity_matrix agregando el nuevo set de canciones
           como PID "pivote". Se deja reservado el PID 0 para este set de canciones.

               - canciones_df: dataframe con una lista de canciones
               - number: número de canciones requeridas para recomendar
               - N: número de playlist cercanas para ir a buscar candidatos de canciones
        """
        # Preproceso para computar el vector de características promedio
        canciones_df = \
                canciones_df.reset_index() \
                [['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
                  'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]

        # Verificar que no haya una lista ya pivoteada 
        if sum(self.avg_features_by_pid_all.pid == 0) != 0:
            track_set = pd.concat([pd.DataFrame({'PID': np.zeros(canciones_df.shape[0], 'int32')}),
                                   canciones_df], axis=1)

            # Se computa el vector de características promedio del set de canciones recibido
            track_set = track_set.groupby('PID').mean().reset_index()
        
            # Concatenar al principio del atributo self.avg_features_by_pid y self.obs_labels
            self.avg_features_by_pid = np.r_[track_set.iloc[:, 1:], self.avg_features_by_pid]
            self.obs_labels = np.r_[0, self.obs_labels]

            # Actualizar matriz de distancia
            self.refit()

        # Actualizar listas mas cercanas (siempre es el PID en la posición 0)
        nearest_index = np.argsort(self.proximity_matrix[0, :])[:N+1][1:]
        self.N_nearest = self.obs_labels[nearest_index]

        # Se cambia el atributo pid_id la cual es la lista objetivo para buscar las recomendaciones
        self.pid_id = 0

        # Entregar recomendaciones
        return self.get_recommendations(num_tracks=number)
    
    def get_recommendations(self, num_tracks=20):
        """Dado un track de canciones arbitarias, se utiliza por el método
           recommend_given_track_set
        """ 
        recommended_songs_list = self.artist[self.artist.pid.isin(self.N_nearest)].copy()
        recommended_songs_list = recommended_songs_list.drop_duplicates(subset=['artist_uri'])

        # Seleccionar solo los features de las canciones
        features_columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 
         'speechiness', 'acousticness', 'instrumentalness', 
         'liveness', 'valence', 'tempo']

        # Obtenemos las canciones candidatas     
        recommended_songs_list['similarity'] = np.dot(recommended_songs_list[features_columns].to_numpy(), 
                                                      self.avg_features_by_pid[0, :].reshape(11, 1))
        recommended_songs_list = recommended_songs_list.sort_values(by=['similarity'], ascending=True)

        # Se eliminan los duplicados.
        recommended_songs_list = recommended_songs_list.drop_duplicates(subset=['artist_uri'])

        # Se retorna el número de canciones, 2: track_uri
        return recommended_songs_list.iloc[:num_tracks, 2]

class Recommender2:
    def __init__(self, var_names):
        self.var_names = var_names
        pass
    
    def train(self, tracks_df, playlists_df):
        self.tracks_df, self.playlists_df = tracks_df, playlists_df
        playlist_ids=list(set(playlists_df["pid"]))
        self.X_ori=np.asarray(tracks_df[self.var_names])
        self.X=(self.X_ori-np.tile(np.mean(self.X_ori, axis=0), (self.X_ori.shape[0], 1)))/np.tile(np.std(self.X_ori, axis=0), (self.X_ori.shape[0], 1))
        self.X_t=PolynomialFeatures(1).fit_transform(self.X)
        self.W=np.zeros(0)
        total=len(playlist_ids)
        self.lists=np.zeros(shape=(len(self.X), total))-1
        for playlist_i in range(total):
            print(playlist_i) if (playlist_i % (total/5))==0 else None
            this_playlist=playlists_df[playlists_df["pid"]==playlist_ids[playlist_i]]
            y=1*tracks_df["uri"].isin(this_playlist["track_uri"])
            if(sum(y))>0:
                self.lists[y==1, playlist_i]=playlist_i
                clf=LogisticRegression(fit_intercept=False)
                clf.fit(self.X_t, y)
                self.W=np.append(self.W, clf.coef_)
        self.lists=np.asarray(self.lists)
        self.W=self.W.reshape(-1, clf.coef_.size)
        ret=np.exp(self.X_t @ self.W.T-10)
        self.probas=ret/np.tile(np.apply_along_axis(sum, 1, ret), (self.W.T.shape[1],1)).T
        
    def recommend_list(self, canciones_df, suavizado=1000, number=100, exclude_same=True):
        canciones=np.asarray(canciones_df[self.var_names])
        canciones=np.asarray(canciones).reshape(-1, 13)
        canciones=(canciones-np.tile(np.mean(self.X_ori, axis=0), (canciones.shape[0], 1)))/np.tile(np.std(self.X_ori, axis=0), (canciones.shape[0], 1))
        canciones_t=PolynomialFeatures(1).fit_transform(canciones)
        matmult=np.exp(canciones_t @ self.W.T-10)
        probas_canciones=matmult/np.tile(np.apply_along_axis(sum, 1, matmult), (self.W.T.shape[1],1)).T
        puntajes=np.zeros(len(self.X))
        not_in_input=np.ones(len(self.X))
        for this_proba in probas_canciones:
            distancia_proba=np.asarray([np.linalg.norm(this_proba-proba) for proba in self.probas])
            not_in_input=not_in_input*(distancia_proba>1e-15)*1 if exclude_same else not_in_input
            order=np.argsort(np.argsort(distancia_proba))
            puntajes+=np.exp(-order*len(canciones)/suavizado)
        puntajes=puntajes*not_in_input if exclude_same else puntajes
        final_order=np.argsort(-puntajes)
        y_recom=np.zeros(len(self.X))
        y_recom[final_order[:number]]=1
        return self.tracks_df.iloc[final_order][:number]["uri"]

# Se crea la clase autoencoder.
class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(11, 10),
            nn.ReLU(),
            nn.Linear(10, 8),
            nn.ReLU(),
            nn.Linear(8, 6),
            nn.ReLU(),
            nn.Linear(6, 4),
            nn.ReLU(),
            nn.Linear(4, 2))
        self.decoder = nn.Sequential(
            nn.Linear(2, 4),
            nn.ReLU(),
            nn.Linear(4, 6),
            nn.ReLU(),
            nn.Linear(6, 8),
            nn.ReLU(),
            nn.Linear(8, 10),
            nn.ReLU(),
            nn.Linear(10, 11))
        
    def predict(self, data):
        return self.encoder(data)

    def forward(self, x):
        encoder = self.encoder(x)
        decoder = self.decoder(encoder)
        return decoder 


# Se crea la clase GenerateDataset para leer los datos.
class GenerateDataset(Dataset):
    def __init__(self, numpy_array):
        self.numpy_array = numpy_array

    def __len__(self):
        return len(self.numpy_array)

    def __getitem__(self, idx):
        data = self.numpy_array[idx]
        x = np.isnan(data)
        data[x] = 0
        return data

class Recommender3:
    def __init__(self, var_names, path="../data/models/modelo_50e_256b_decay.pth"):
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.model = Autoencoder().to(self.device)
        self.model.load_state_dict(torch.load(path, map_location=self.device))
        self.data = None
        self.processed_data = []
        self.processed_data_df = None
        self.scaler = StandardScaler()
        self.var_names = var_names
        
    def load_data(self, tracks_val):
        self.scaler.fit(tracks_val[self.var_names[:-2]])
        tracks_val_np = self.scaler.transform(tracks_val[self.var_names[:-2]])
        self.data = DataLoader(GenerateDataset(tracks_val_np.astype('f')),
                    batch_size=1, shuffle=False)
        
        for data in self.data:
            data = data.to(self.device)
            self.processed_data.append(self.model.predict(data).detach().cpu().numpy()[0])
        
        self.processed_data_df = pd.DataFrame(self.processed_data, columns=['comp_1','comp_2'])
        self.processed_data_df = self.processed_data_df.assign(uri=tracks_val['uri'])
    
    def recommend_list(self, canciones_df, number=100, **kwargs):
        canciones_np = self.scaler.transform(canciones_df[self.var_names[:-2]])
        canciones_dl = DataLoader(GenerateDataset(canciones_np.astype('f')),
                    batch_size=1, shuffle=False)
        
        data_inference = []
        for data in canciones_dl:
            data = data.to(self.device)
            data_inference.append(self.model.predict(data).detach().cpu().numpy()[0])
        
        data_inference_df = pd.DataFrame(data_inference, columns=['comp_1','comp_2'])
        canciones_df = canciones_df.reset_index()
        data_inference_df = data_inference_df.assign(uri=canciones_df["uri"])
        
        # inferencia
        recommendations = []
        amount = int(number/canciones_df.shape[0]) + 5
        for i in range(canciones_df.shape[0]):
            # Se toma la primera playlist/cancion y se pasa a tensor.
            playlist_input = torch.tensor(data_inference_df.iloc[i:i+1,:2].to_numpy())
            
            # processed_data_df son las canciones procesadas por .encoder (espacio latente).
            dataset_latente = torch.tensor(self.processed_data_df.iloc[:,:2].to_numpy())

            # Se buscan las canciones mas cercanas a la playlist/cancion de input.
            result_cdist = torch.cdist(playlist_input, dataset_latente, p=2)

            # Se ordenan los valores.
            result_cdist_sort = [x.item() for x in np.argsort(result_cdist)[0]][:amount]
            recommendations.extend(result_cdist_sort)
            
        return self.processed_data_df.iloc[recommendations[1:number+1], 2]