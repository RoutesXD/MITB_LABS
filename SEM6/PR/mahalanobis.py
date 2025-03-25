import numpy as np
from scipy.spatial.distance import mahalanobis

def compute_mahalanobis_distance_between_polygons(polygon1, polygon2):
    poly1_array = np.array(polygon1)
    poly2_array = np.array(polygon2)
    centroid1 = np.mean(poly1_array, axis=0)
    centroid2 = np.mean(poly2_array, axis=0)
    combined_points = np.vstack((poly1_array, poly2_array))
    covariance_matrix = np.cov(combined_points.T)

    try:
        inv_cov_matrix = np.linalg.inv(covariance_matrix)
    except np.linalg.LinAlgError:
        raise ValueError("Covariance matrix is singular and cannot be inverted. Ensure the polygons are not collinear.")

    return mahalanobis(centroid1, centroid2, inv_cov_matrix)

if __name__ == "__main__":
    def get_polygon_input(polygon_num):
        print(f"Enter the coordinates of Polygon {polygon_num} (e.g., x1 y1, x2 y2, ...):")
        points = input("Coordinates: ").strip().split(",")
        return [tuple(map(float, point.strip().split())) for point in points]

    try:
        polygon1 = get_polygon_input(1)
        polygon2 = get_polygon_input(2)
        distance = compute_mahalanobis_distance_between_polygons(polygon1, polygon2)
        print(f"Mahalanobis Distance between the polygons: {distance}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
