import numpy as np
import open3d as o3d
import pye57


def read_e57(filepath):
    pc = pye57.E57(filepath)
    np_arrays = pc.read_scan(0, ignore_missing_fields=True)
    xyz = np.zeros((np.size(np_arrays["cartesianX"]), 3))
    xyz[:, 0] = np.reshape(np_arrays["cartesianX"], -1)
    xyz[:, 1] = np.reshape(np_arrays["cartesianY"], -1)
    xyz[:, 2] = np.reshape(np_arrays["cartesianZ"], -1)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    return pcd


def visualise_pointcloud(pcd):
    pcd.paint_uniform_color([0.5, 0.5, 0.5])
    pcd.estimate_normals()
    pcd.orient_normals_consistent_tangent_plane(1)
    o3d.visualization.draw([pcd])


if __name__ == "__main__":
    pcd = read_e57(
        r"C:\Users\Graham Knapp\PycharmProjects\e57py\testdata\bunnyFloat.e57"
    )
    visualise_pointcloud(pcd)
