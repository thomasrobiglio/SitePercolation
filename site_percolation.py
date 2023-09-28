import numpy as np

class site_percolation:
     def  __init__(self, N, p):
          self.N = N
          self.p = p
          self.grid = np.zeros((N,N))
          self.clusters = {}

     def run_percolation(self):
          for i in range(self.N):
               for j in range(self.N):
                    if np.random.rand() < self.p:
                         self.grid[i,j] = 1
     
     def get_grid(self):
          return self.grid.copy()

     def assign_clusters(self):
          def dfs(matrix, cluster, start_row, start_col, cluster_id):
               stack = [(start_row, start_col)]
               while stack:
                    row, col = stack.pop()
                    if matrix[row,col] == 1:
                         matrix[row,col] = cluster_id
                         cluster.append((row,col))
                         if row > 0:
                              stack.append((row-1, col))
                         if row < self.N-1:
                              stack.append((row+1, col))
                         if col > 0:
                              stack.append((row, col-1))
                         if col < self.N-1:
                              stack.append((row, col+1))
          
          self.clusters = {}
          cluster_id = 2

          for i in range(self.N):
               for j in range(self.N):
                    if self.grid[i,j] == 1:
                         cluster = []
                         dfs(matrix=self.grid, cluster=cluster, start_row=i, start_col=j, cluster_id=cluster_id)
                         self.clusters[cluster_id] = cluster
                         cluster_id += 1
               return

          
     def get_clusters(self):
          return self.clusters.copy()
     
     def check_percolation(self):
          if self.clusters == {}:
               self.assign_clusters()
          # find the larqest cluster
          largest_cluster = []
          for cluster in self.clusters.values():
               if len(cluster) > len(largest_cluster):
                    largest_cluster = cluster
          # check if the largest cluster spans the grid
          for i in range(self.N):
               if (self.N-1, i) in largest_cluster:
                    return True
          
          return False
     
     def get_p_inf(self):
          if self.check_percolation():
               largest_cluster = []
               for cluster in self.clusters.values():
                    if len(cluster) > len(largest_cluster):
                         largest_cluster = cluster
               return len(largest_cluster)/(self.N**2)
          else:
               return 0


     
               



