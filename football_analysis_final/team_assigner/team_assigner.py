from sklearn.cluster import KMeans
import numpy as np

class TeamAssigner:
    def __init__(self):
        """Store learned team colors and per-player team assignments."""
        self.team_colors = {}
        self.player_team_dict = {}
    
    def get_clustering_model(self,image):
        """Fit a 2-cluster KMeans model on image pixels."""
        # Reshape the image to 2D array
        image_2d = image.reshape(-1,3)

        # Preform K-means with 2 clusters
        kmeans = KMeans(n_clusters=2, init="k-means++",n_init=1)
        kmeans.fit(image_2d)

        return kmeans

    def get_player_color(self,frame,bbox):
        """Estimate dominant jersey color from the player's upper-body crop."""
        image = frame[int(bbox[1]):int(bbox[3]),int(bbox[0]):int(bbox[2])]

        if image.size == 0:
            return np.array([0.0, 0.0, 0.0])

        top_half_image = image[0:int(image.shape[0]/2),:]
        if top_half_image.size == 0:
            return np.array([0.0, 0.0, 0.0])

        # Get Clustering model
        kmeans = self.get_clustering_model(top_half_image)

        # Get the cluster labels forr each pixel
        labels = kmeans.labels_

        # Reshape the labels to the image shape
        clustered_image = labels.reshape(top_half_image.shape[0],top_half_image.shape[1])

        # Get the player cluster
        corner_clusters = [clustered_image[0,0],clustered_image[0,-1],clustered_image[-1,0],clustered_image[-1,-1]]
        non_player_cluster = max(set(corner_clusters),key=corner_clusters.count)
        player_cluster = 1 - non_player_cluster

        player_color = kmeans.cluster_centers_[player_cluster]

        return player_color


    def assign_team_color(self,frame, player_detections):
        """Learn two team color centroids from current player detections."""
        
        player_colors = []
        for _, player_detection in player_detections.items():
            bbox = player_detection["bbox"]
            player_color =  self.get_player_color(frame,bbox)
            player_colors.append(player_color)

        if len(player_colors) == 0:
            self.team_colors[1] = np.array([255.0, 0.0, 0.0])
            self.team_colors[2] = np.array([0.0, 0.0, 255.0])
            self.kmeans = None
            return

        if len(player_colors) == 1:
            self.team_colors[1] = player_colors[0]
            self.team_colors[2] = player_colors[0]
            self.kmeans = None
            return
        
        kmeans = KMeans(n_clusters=2, init="k-means++",n_init=10)
        kmeans.fit(player_colors)

        self.kmeans = kmeans

        self.team_colors[1] = kmeans.cluster_centers_[0]
        self.team_colors[2] = kmeans.cluster_centers_[1]


    def get_player_team(self,frame,player_bbox,player_id):
        """Predict and cache team ID for a player using learned color clusters."""
        if player_id in self.player_team_dict:
            return self.player_team_dict[player_id]

        if not hasattr(self, 'kmeans') or self.kmeans is None:
            self.player_team_dict[player_id] = 1
            return 1

        player_color = self.get_player_color(frame,player_bbox)

        team_id = self.kmeans.predict(player_color.reshape(1,-1))[0]
        team_id+=1

        if player_id ==91:
            team_id=1

        self.player_team_dict[player_id] = team_id

        return team_id
