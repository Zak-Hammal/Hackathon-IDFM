import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from ast import literal_eval

class UserClustering:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        
    def _process_text_column(self, column):
        """Encode les colonnes textuelles"""
        if column.name not in self.label_encoders:
            self.label_encoders[column.name] = LabelEncoder()
        return self.label_encoders[column.name].fit_transform(column)
    

    def explode_columns_with_lists(self, df):
        """
        Explose les colonnes contenant des listes dans un DataFrame.
        
        Args:
        - df (pd.DataFrame): Le DataFrame à traiter.

        Returns:
        - pd.DataFrame: Le DataFrame avec les colonnes de listes éclatées.
        """
        new_df = df.copy()  # Copie pour ne pas modifier l'original
        for col in new_df.columns:
            print(col, new_df[col].dtype)
            # Vérifie si tous les éléments de la colonne sont des listes
            if new_df[col].str.contains(r'[\[\{]').any():

                # Trouver la longueur maximale des listes dans cette colonne
                max_length = new_df[col].apply(len).max()
                print(max_length)
                
                # Créer autant de nouvelles colonnes qu'il y a de valeurs dans les listes
                for i in range(max_length):
                    new_df[f"{col}_{i}"] = new_df[col].apply(lambda x: x[i] if i < len(x) else None)
                
                # Supprimer la colonne d'origine
                new_df.drop(columns=[col], inplace=True)
        return new_df

    
    def _detect_and_process_column(self, column):
        """Détecte et traite chaque type de colonne"""
        if column.dtype == 'object':
            try:
                # Essaie de convertir en nombre
                return pd.to_numeric(column)
            except:
                # Vérifie si c'est une liste
                if column.str.contains(r'[\[\{]').any():
                    list_df = self._process_list_column(column)
                    # Retourner uniquement la première colonne pour maintenir la compatibilité
                    return list_df.iloc[:, 0]
                else:
                    return self._process_text_column(column)
        return column
    
    def fit_transform(self, df):
        """Transforme le dataframe et effectue le clustering"""
        # Copie du dataframe
        processed_df = pd.DataFrame()
        processed_df['user_id'] = df['user_id']
        
        # Traitement de chaque colonne sauf user_id
        feature_columns = [col for col in df.columns if col != 'user_id']
        for col in feature_columns:
            result = self._detect_and_process_column(df[col])
            print(result)
            if isinstance(result, pd.DataFrame):
                # Si le résultat est un DataFrame (cas des listes), ajouter toutes les colonnes
                for new_col in result.columns:
                    processed_df[new_col] = result[new_col]
                    print(new_col, result[new_col].dtype)
            else:
                # Sinon, ajouter la colonne directement
                processed_df[col] = result
        
        # Normalisation des données
        #features = processed_df.drop('user_id', axis=1).values
        #scaled_features = self.scaler.fit_transform(features)
        
        # Application du clustering
        #clusters = self.kmeans.fit_predict(scaled_features)
        
        # Création du résultat
        #result = pd.DataFrame({
        #    'user_id': df['user_id'],
        #    'cluster': clusters
        #})
        
        return processed_df

df = pd.read_csv('./data/data_generic.csv', sep=';')
clusterer = UserClustering(n_clusters=3)
new_df = clusterer.explode_columns_with_lists(df)
print(new_df)

# Exemple d'utilisation
if __name__ == "__main__":
    df = pd.read_csv('./data/data_generic.csv', sep=';')
    clustered_df = cluster_users(df)
    print(clustered_df)

