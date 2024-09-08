import math
import numpy as np

def haversine(lat1, lon1, lat2, lon2):
    # 지구의 반지름 (미터)
    if lat1 == np.nan or lat2 == np.nan or lon1 == np.nan or lon2 == np.nan:
        return np.nan

    R = 6371000  

    # 위도와 경도를 라디안으로 변환
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Haversine 공식 계산
    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # 거리 계산
    distance = R * c
    return distance / 1000 ## m to km