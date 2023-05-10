import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.cluster import KMeans, DBSCAN, OPTICS
from sklearn.preprocessing import StandardScaler

vis = o3d.visualization.Visualizer()
vis.create_window()

# #1
# pcd = o3d.io.read_point_cloud('TLS_kitchen_sample.ply')
#
#
# # #RANSAC
# pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1,
#                                                                        max_nn=16),
#                      fast_normal_computation=True)
#
# plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
#                                          ransac_n=3,
#                                          num_iterations=1000)
# inlier_cloud = pcd.select_by_index(inliers)
# outlier_cloud = pcd.select_by_index(inliers, invert=True)
#
# inlier_cloud.paint_uniform_color([1, 0, 0])
# outlier_cloud.paint_uniform_color([0.6, 0.6, 0.6])
#
# # o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])
# #DBSCAN
# labels = np.array(pcd.cluster_dbscan(eps=0.05, min_points=10))
#
# max_label = labels.max()
# colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
# colors[labels < 0] = 0
# pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
# o3d.visualization.draw_geometries([pcd])

# #2
#
# pcd = o3d.io.read_point_cloud('TLS_kitchen.ply')
# pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1,
#                                                                        max_nn=16),
#                      fast_normal_computation=True)
# # #Multi-RANSAC
# # segment_models = {}
# # segments = {}
# # max_plane_idx = 10
# # rest = pcd
# # for i in range(max_plane_idx):
# #     colors = plt.get_cmap("tab20")(i)
# #     segment_models[i], inliers = rest.segment_plane(distance_threshold=0.01,ransac_n=3,num_iterations=1000)
# #     segments[i]=rest.select_by_index(inliers)
# #     segments[i].paint_uniform_color(list(colors[:3]))
# #     rest = rest.select_by_index(inliers, invert=True)
# #     print("pass", i, "/", max_plane_idx, "done.")
# #
# # o3d.visualization.draw_geometries([segments[i] for i in range(max_plane_idx)]+[rest])
#
# #Euclid-RANSAC
# segment_models = {}
# segments = {}
# max_plane_idx = 20
# rest = pcd
# d_threshold = 0.01
# for i in range(max_plane_idx):
#     colors = plt.get_cmap("tab20")(i)
#     segment_models[i], inliers = rest.segment_plane(distance_threshold=0.01,
#                                                     ransac_n=3,
#                                                     num_iterations=1000)
#     segments[i] = rest.select_by_index(inliers)
#     labels = np.array(segments[i].cluster_dbscan(eps=d_threshold*10, min_points=10))
#     candidates = [len(np.where(labels == j)[0]) for j in np.unique(labels)]
#     best_candidate = int(np.unique(labels)[np.where(candidates == np.max(candidates))[0]])
#     print("the best candidate is: ", best_candidate)
#     rest = rest.select_by_index(inliers, invert=True) + segments[i].select_by_index(
#         list(np.where(labels != best_candidate)[0]))
#     segments[i] = segments[i].select_by_index(list(np.where(labels == best_candidate)[0]))
#     segments[i].paint_uniform_color(list(colors[:3]))
#     print("pass", i+1, "/", max_plane_idx, "done.")
#
# #DBSCAN
# labels = np.array(rest.cluster_dbscan(eps=0.05, min_points=5))
# max_label = labels.max()
# print(f"point cloud has {max_label + 1} clusters")
#
# colors = plt.get_cmap("tab10")(labels / (max_label if max_label > 0 else 1))
# colors[labels < 0] = 0
# rest.colors = o3d.utility.Vector3dVector(colors[:, :3])
#
# #o3d.visualization.draw_geometries([segments[i] for i in range(max_plane_idx)]+[rest])
# o3d.visualization.draw_geometries([segments[i] for i in range(max_plane_idx)]+[rest],
#                                   zoom=0.3199,
#                                   front=[0.30159062875123849, 0.94077325609922868, 0.15488309545553303],
#                                   lookat=[-3.9559999108314514, -0.055000066757202148, -0.27599999308586121],
#                                   up=[-0.044411423633999815, -0.138726419067636, 0.98753122516983349])


#################################k-means##############################
#
# pcd = o3d.io.read_point_cloud('TLS_kitchen_sample.ply')
# pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1,
#                                                                        max_nn=16),
#                      fast_normal_computation=True)
#
# points = np.asarray(pcd.points).copy()
#
# scaled_points = StandardScaler().fit_transform(points)
#
# model = KMeans(n_clusters=5)
# model.fit(scaled_points)
#
# # model = DBSCAN(eps=0.15, min_samples=10)
# # model.fit(scaled_points)
#
# labels = model.labels_
# n_clusters = len(set(labels))
# colors = plt.get_cmap("tab20")(labels / (n_clusters if n_clusters > 0 else 1))
# colors[labels < 0] = 0
# pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
# o3d.visualization.draw_geometries([pcd])


