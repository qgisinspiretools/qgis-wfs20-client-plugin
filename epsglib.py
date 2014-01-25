"""
/***************************************************************************
 EPSG Library
                             -------------------
        begin                : 2012-05-17
        copyright            : (C) 2012 by Juergen Weichand
        email                : juergen@weichand.de
        website              : http://www.weichand.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

epsg_lat_lon_order = frozenset([

    # Based on EPSG-Registry 8.2 (2013-04-29) PostgreSQL-Dump
    #   SELECT
    #   r.coord_ref_sys_code || ', # '|| r.coord_ref_sys_name as output
    #   FROM epsg_coordinateaxis as a, epsg_coordinatereferencesystem as r
    #   WHERE a.coord_sys_code = r.coord_sys_code AND coord_axis_orientation = 'north' AND coord_axis_order = 1
    #   ORDER BY r.coord_ref_sys_code;

    2036, # NAD83(CSRS98) / New Brunswick Stereo
    2044, # Hanoi 1972 / Gauss-Kruger zone 18
    2045, # Hanoi 1972 / Gauss-Kruger zone 19
    2081, # Chos Malal 1914 / Argentina 2
    2082, # Pampa del Castillo / Argentina 2
    2083, # Hito XVIII 1963 / Argentina 2
    2085, # NAD27 / Cuba Norte
    2086, # NAD27 / Cuba Sur
    2091, # South Yemen / Gauss Kruger zone 8
    2092, # South Yemen / Gauss Kruger zone 9
    2093, # Hanoi 1972 / GK 106 NE
    2096, # Korean 1985 / East Belt
    2097, # Korean 1985 / Central Belt
    2098, # Korean 1985 / West Belt
    2105, # NZGD2000 / Mount Eden 2000
    2106, # NZGD2000 / Bay of Plenty 2000
    2107, # NZGD2000 / Poverty Bay 2000
    2108, # NZGD2000 / Hawkes Bay 2000
    2109, # NZGD2000 / Taranaki 2000
    2110, # NZGD2000 / Tuhirangi 2000
    2111, # NZGD2000 / Wanganui 2000
    2112, # NZGD2000 / Wairarapa 2000
    2113, # NZGD2000 / Wellington 2000
    2114, # NZGD2000 / Collingwood 2000
    2115, # NZGD2000 / Nelson 2000
    2116, # NZGD2000 / Karamea 2000
    2117, # NZGD2000 / Buller 2000
    2118, # NZGD2000 / Grey 2000
    2119, # NZGD2000 / Amuri 2000
    2120, # NZGD2000 / Marlborough 2000
    2121, # NZGD2000 / Hokitika 2000
    2122, # NZGD2000 / Okarito 2000
    2123, # NZGD2000 / Jacksons Bay 2000
    2124, # NZGD2000 / Mount Pleasant 2000
    2125, # NZGD2000 / Gawler 2000
    2126, # NZGD2000 / Timaru 2000
    2127, # NZGD2000 / Lindis Peak 2000
    2128, # NZGD2000 / Mount Nicholas 2000
    2129, # NZGD2000 / Mount York 2000
    2130, # NZGD2000 / Observation Point 2000
    2131, # NZGD2000 / North Taieri 2000
    2132, # NZGD2000 / Bluff 2000
    2166, # Pulkovo 1942(83) / Gauss Kruger zone 3
    2167, # Pulkovo 1942(83) / Gauss Kruger zone 4
    2168, # Pulkovo 1942(83) / Gauss Kruger zone 5
    2169, # Luxembourg 1930 / Gauss
    2170, # MGI / Slovenia Grid
    2171, # Pulkovo 1942(58) / Poland zone I
    2172, # Pulkovo 1942(58) / Poland zone II
    2173, # Pulkovo 1942(58) / Poland zone III
    2174, # Pulkovo 1942(58) / Poland zone IV
    2175, # Pulkovo 1942(58) / Poland zone V
    2176, # ETRS89 / Poland CS2000 zone 5
    2177, # ETRS89 / Poland CS2000 zone 6
    2178, # ETRS89 / Poland CS2000 zone 7
    2179, # ETRS89 / Poland CS2000 zone 8
    2180, # ETRS89 / Poland CS92
    2193, # NZGD2000 / New Zealand Transverse Mercator 2000
    2199, # Albanian 1987 / Gauss Kruger zone 4
    2200, # ATS77 / New Brunswick Stereographic (ATS77)
    2206, # ED50 / 3-degree Gauss-Kruger zone 9
    2207, # ED50 / 3-degree Gauss-Kruger zone 10
    2208, # ED50 / 3-degree Gauss-Kruger zone 11
    2209, # ED50 / 3-degree Gauss-Kruger zone 12
    2210, # ED50 / 3-degree Gauss-Kruger zone 13
    2211, # ED50 / 3-degree Gauss-Kruger zone 14
    2212, # ED50 / 3-degree Gauss-Kruger zone 15
    2218, # Scoresbysund 1952 / Greenland zone 5 east
    2221, # Scoresbysund 1952 / Greenland zone 6 east
    2296, # Ammassalik 1958 / Greenland zone 7 east
    2297, # Qornoq 1927 / Greenland zone 1 east
    2298, # Qornoq 1927 / Greenland zone 2 east
    2299, # Qornoq 1927 / Greenland zone 2 west
    2300, # Qornoq 1927 / Greenland zone 3 east
    2301, # Qornoq 1927 / Greenland zone 3 west
    2302, # Qornoq 1927 / Greenland zone 4 east
    2303, # Qornoq 1927 / Greenland zone 4 west
    2304, # Qornoq 1927 / Greenland zone 5 west
    2305, # Qornoq 1927 / Greenland zone 6 west
    2306, # Qornoq 1927 / Greenland zone 7 west
    2307, # Qornoq 1927 / Greenland zone 8 east
    2319, # ED50 / TM27
    2320, # ED50 / TM30
    2321, # ED50 / TM33
    2322, # ED50 / TM36
    2323, # ED50 / TM39
    2324, # ED50 / TM42
    2325, # ED50 / TM45
    2326, # Hong Kong 1980 Grid System
    2327, # Xian 1980 / Gauss-Kruger zone 13
    2328, # Xian 1980 / Gauss-Kruger zone 14
    2329, # Xian 1980 / Gauss-Kruger zone 15
    2330, # Xian 1980 / Gauss-Kruger zone 16
    2331, # Xian 1980 / Gauss-Kruger zone 17
    2332, # Xian 1980 / Gauss-Kruger zone 18
    2333, # Xian 1980 / Gauss-Kruger zone 19
    2334, # Xian 1980 / Gauss-Kruger zone 20
    2335, # Xian 1980 / Gauss-Kruger zone 21
    2336, # Xian 1980 / Gauss-Kruger zone 22
    2337, # Xian 1980 / Gauss-Kruger zone 23
    2338, # Xian 1980 / Gauss-Kruger CM 75E
    2339, # Xian 1980 / Gauss-Kruger CM 81E
    2340, # Xian 1980 / Gauss-Kruger CM 87E
    2341, # Xian 1980 / Gauss-Kruger CM 93E
    2342, # Xian 1980 / Gauss-Kruger CM 99E
    2343, # Xian 1980 / Gauss-Kruger CM 105E
    2344, # Xian 1980 / Gauss-Kruger CM 111E
    2345, # Xian 1980 / Gauss-Kruger CM 117E
    2346, # Xian 1980 / Gauss-Kruger CM 123E
    2347, # Xian 1980 / Gauss-Kruger CM 129E
    2348, # Xian 1980 / Gauss-Kruger CM 135E
    2349, # Xian 1980 / 3-degree Gauss-Kruger zone 25
    2350, # Xian 1980 / 3-degree Gauss-Kruger zone 26
    2351, # Xian 1980 / 3-degree Gauss-Kruger zone 27
    2352, # Xian 1980 / 3-degree Gauss-Kruger zone 28
    2353, # Xian 1980 / 3-degree Gauss-Kruger zone 29
    2354, # Xian 1980 / 3-degree Gauss-Kruger zone 30
    2355, # Xian 1980 / 3-degree Gauss-Kruger zone 31
    2356, # Xian 1980 / 3-degree Gauss-Kruger zone 32
    2357, # Xian 1980 / 3-degree Gauss-Kruger zone 33
    2358, # Xian 1980 / 3-degree Gauss-Kruger zone 34
    2359, # Xian 1980 / 3-degree Gauss-Kruger zone 35
    2360, # Xian 1980 / 3-degree Gauss-Kruger zone 36
    2361, # Xian 1980 / 3-degree Gauss-Kruger zone 37
    2362, # Xian 1980 / 3-degree Gauss-Kruger zone 38
    2363, # Xian 1980 / 3-degree Gauss-Kruger zone 39
    2364, # Xian 1980 / 3-degree Gauss-Kruger zone 40
    2365, # Xian 1980 / 3-degree Gauss-Kruger zone 41
    2366, # Xian 1980 / 3-degree Gauss-Kruger zone 42
    2367, # Xian 1980 / 3-degree Gauss-Kruger zone 43
    2368, # Xian 1980 / 3-degree Gauss-Kruger zone 44
    2369, # Xian 1980 / 3-degree Gauss-Kruger zone 45
    2370, # Xian 1980 / 3-degree Gauss-Kruger CM 75E
    2371, # Xian 1980 / 3-degree Gauss-Kruger CM 78E
    2372, # Xian 1980 / 3-degree Gauss-Kruger CM 81E
    2373, # Xian 1980 / 3-degree Gauss-Kruger CM 84E
    2374, # Xian 1980 / 3-degree Gauss-Kruger CM 87E
    2375, # Xian 1980 / 3-degree Gauss-Kruger CM 90E
    2376, # Xian 1980 / 3-degree Gauss-Kruger CM 93E
    2377, # Xian 1980 / 3-degree Gauss-Kruger CM 96E
    2378, # Xian 1980 / 3-degree Gauss-Kruger CM 99E
    2379, # Xian 1980 / 3-degree Gauss-Kruger CM 102E
    2380, # Xian 1980 / 3-degree Gauss-Kruger CM 105E
    2381, # Xian 1980 / 3-degree Gauss-Kruger CM 108E
    2382, # Xian 1980 / 3-degree Gauss-Kruger CM 111E
    2383, # Xian 1980 / 3-degree Gauss-Kruger CM 114E
    2384, # Xian 1980 / 3-degree Gauss-Kruger CM 117E
    2385, # Xian 1980 / 3-degree Gauss-Kruger CM 120E
    2386, # Xian 1980 / 3-degree Gauss-Kruger CM 123E
    2387, # Xian 1980 / 3-degree Gauss-Kruger CM 126E
    2388, # Xian 1980 / 3-degree Gauss-Kruger CM 129E
    2389, # Xian 1980 / 3-degree Gauss-Kruger CM 132E
    2390, # Xian 1980 / 3-degree Gauss-Kruger CM 135E
    2391, # KKJ / Finland zone 1
    2392, # KKJ / Finland zone 2
    2393, # KKJ / Finland Uniform Coordinate System
    2394, # KKJ / Finland zone 4
    2395, # South Yemen / Gauss-Kruger zone 8
    2396, # South Yemen / Gauss-Kruger zone 9
    2397, # Pulkovo 1942(83) / 3-degree Gauss-Kruger zone 3
    2398, # Pulkovo 1942(83) / 3-degree Gauss-Kruger zone 4
    2399, # Pulkovo 1942(83) / 3-degree Gauss-Kruger zone 5
    2400, # RT90 2.5 gon W
    2401, # Beijing 1954 / 3-degree Gauss-Kruger zone 25
    2402, # Beijing 1954 / 3-degree Gauss-Kruger zone 26
    2403, # Beijing 1954 / 3-degree Gauss-Kruger zone 27
    2404, # Beijing 1954 / 3-degree Gauss-Kruger zone 28
    2405, # Beijing 1954 / 3-degree Gauss-Kruger zone 29
    2406, # Beijing 1954 / 3-degree Gauss-Kruger zone 30
    2407, # Beijing 1954 / 3-degree Gauss-Kruger zone 31
    2408, # Beijing 1954 / 3-degree Gauss-Kruger zone 32
    2409, # Beijing 1954 / 3-degree Gauss-Kruger zone 33
    2410, # Beijing 1954 / 3-degree Gauss-Kruger zone 34
    2411, # Beijing 1954 / 3-degree Gauss-Kruger zone 35
    2412, # Beijing 1954 / 3-degree Gauss-Kruger zone 36
    2413, # Beijing 1954 / 3-degree Gauss-Kruger zone 37
    2414, # Beijing 1954 / 3-degree Gauss-Kruger zone 38
    2415, # Beijing 1954 / 3-degree Gauss-Kruger zone 39
    2416, # Beijing 1954 / 3-degree Gauss-Kruger zone 40
    2417, # Beijing 1954 / 3-degree Gauss-Kruger zone 41
    2418, # Beijing 1954 / 3-degree Gauss-Kruger zone 42
    2419, # Beijing 1954 / 3-degree Gauss-Kruger zone 43
    2420, # Beijing 1954 / 3-degree Gauss-Kruger zone 44
    2421, # Beijing 1954 / 3-degree Gauss-Kruger zone 45
    2422, # Beijing 1954 / 3-degree Gauss-Kruger CM 75E
    2423, # Beijing 1954 / 3-degree Gauss-Kruger CM 78E
    2424, # Beijing 1954 / 3-degree Gauss-Kruger CM 81E
    2425, # Beijing 1954 / 3-degree Gauss-Kruger CM 84E
    2426, # Beijing 1954 / 3-degree Gauss-Kruger CM 87E
    2427, # Beijing 1954 / 3-degree Gauss-Kruger CM 90E
    2428, # Beijing 1954 / 3-degree Gauss-Kruger CM 93E
    2429, # Beijing 1954 / 3-degree Gauss-Kruger CM 96E
    2430, # Beijing 1954 / 3-degree Gauss-Kruger CM 99E
    2431, # Beijing 1954 / 3-degree Gauss-Kruger CM 102E
    2432, # Beijing 1954 / 3-degree Gauss-Kruger CM 105E
    2433, # Beijing 1954 / 3-degree Gauss-Kruger CM 108E
    2434, # Beijing 1954 / 3-degree Gauss-Kruger CM 111E
    2435, # Beijing 1954 / 3-degree Gauss-Kruger CM 114E
    2436, # Beijing 1954 / 3-degree Gauss-Kruger CM 117E
    2437, # Beijing 1954 / 3-degree Gauss-Kruger CM 120E
    2438, # Beijing 1954 / 3-degree Gauss-Kruger CM 123E
    2439, # Beijing 1954 / 3-degree Gauss-Kruger CM 126E
    2440, # Beijing 1954 / 3-degree Gauss-Kruger CM 129E
    2441, # Beijing 1954 / 3-degree Gauss-Kruger CM 132E
    2442, # Beijing 1954 / 3-degree Gauss-Kruger CM 135E
    2443, # JGD2000 / Japan Plane Rectangular CS I
    2444, # JGD2000 / Japan Plane Rectangular CS II
    2445, # JGD2000 / Japan Plane Rectangular CS III
    2446, # JGD2000 / Japan Plane Rectangular CS IV
    2447, # JGD2000 / Japan Plane Rectangular CS V
    2448, # JGD2000 / Japan Plane Rectangular CS VI
    2449, # JGD2000 / Japan Plane Rectangular CS VII
    2450, # JGD2000 / Japan Plane Rectangular CS VIII
    2451, # JGD2000 / Japan Plane Rectangular CS IX
    2452, # JGD2000 / Japan Plane Rectangular CS X
    2453, # JGD2000 / Japan Plane Rectangular CS XI
    2454, # JGD2000 / Japan Plane Rectangular CS XII
    2455, # JGD2000 / Japan Plane Rectangular CS XIII
    2456, # JGD2000 / Japan Plane Rectangular CS XIV
    2457, # JGD2000 / Japan Plane Rectangular CS XV
    2458, # JGD2000 / Japan Plane Rectangular CS XVI
    2459, # JGD2000 / Japan Plane Rectangular CS XVII
    2460, # JGD2000 / Japan Plane Rectangular CS XVIII
    2461, # JGD2000 / Japan Plane Rectangular CS XIX
    2462, # Albanian 1987 / Gauss-Kruger zone 4
    2463, # Pulkovo 1995 / Gauss-Kruger CM 21E
    2464, # Pulkovo 1995 / Gauss-Kruger CM 27E
    2465, # Pulkovo 1995 / Gauss-Kruger CM 33E
    2466, # Pulkovo 1995 / Gauss-Kruger CM 39E
    2467, # Pulkovo 1995 / Gauss-Kruger CM 45E
    2468, # Pulkovo 1995 / Gauss-Kruger CM 51E
    2469, # Pulkovo 1995 / Gauss-Kruger CM 57E
    2470, # Pulkovo 1995 / Gauss-Kruger CM 63E
    2471, # Pulkovo 1995 / Gauss-Kruger CM 69E
    2472, # Pulkovo 1995 / Gauss-Kruger CM 75E
    2473, # Pulkovo 1995 / Gauss-Kruger CM 81E
    2474, # Pulkovo 1995 / Gauss-Kruger CM 87E
    2475, # Pulkovo 1995 / Gauss-Kruger CM 93E
    2476, # Pulkovo 1995 / Gauss-Kruger CM 99E
    2477, # Pulkovo 1995 / Gauss-Kruger CM 105E
    2478, # Pulkovo 1995 / Gauss-Kruger CM 111E
    2479, # Pulkovo 1995 / Gauss-Kruger CM 117E
    2480, # Pulkovo 1995 / Gauss-Kruger CM 123E
    2481, # Pulkovo 1995 / Gauss-Kruger CM 129E
    2482, # Pulkovo 1995 / Gauss-Kruger CM 135E
    2483, # Pulkovo 1995 / Gauss-Kruger CM 141E
    2484, # Pulkovo 1995 / Gauss-Kruger CM 147E
    2485, # Pulkovo 1995 / Gauss-Kruger CM 153E
    2486, # Pulkovo 1995 / Gauss-Kruger CM 159E
    2487, # Pulkovo 1995 / Gauss-Kruger CM 165E
    2488, # Pulkovo 1995 / Gauss-Kruger CM 171E
    2489, # Pulkovo 1995 / Gauss-Kruger CM 177E
    2490, # Pulkovo 1995 / Gauss-Kruger CM 177W
    2491, # Pulkovo 1995 / Gauss-Kruger CM 171W
    2492, # Pulkovo 1942 / Gauss-Kruger CM 9E
    2493, # Pulkovo 1942 / Gauss-Kruger CM 15E
    2494, # Pulkovo 1942 / Gauss-Kruger CM 21E
    2495, # Pulkovo 1942 / Gauss-Kruger CM 27E
    2496, # Pulkovo 1942 / Gauss-Kruger CM 33E
    2497, # Pulkovo 1942 / Gauss-Kruger CM 39E
    2498, # Pulkovo 1942 / Gauss-Kruger CM 45E
    2499, # Pulkovo 1942 / Gauss-Kruger CM 51E
    2500, # Pulkovo 1942 / Gauss-Kruger CM 57E
    2501, # Pulkovo 1942 / Gauss-Kruger CM 63E
    2502, # Pulkovo 1942 / Gauss-Kruger CM 69E
    2503, # Pulkovo 1942 / Gauss-Kruger CM 75E
    2504, # Pulkovo 1942 / Gauss-Kruger CM 81E
    2505, # Pulkovo 1942 / Gauss-Kruger CM 87E
    2506, # Pulkovo 1942 / Gauss-Kruger CM 93E
    2507, # Pulkovo 1942 / Gauss-Kruger CM 99E
    2508, # Pulkovo 1942 / Gauss-Kruger CM 105E
    2509, # Pulkovo 1942 / Gauss-Kruger CM 111E
    2510, # Pulkovo 1942 / Gauss-Kruger CM 117E
    2511, # Pulkovo 1942 / Gauss-Kruger CM 123E
    2512, # Pulkovo 1942 / Gauss-Kruger CM 129E
    2513, # Pulkovo 1942 / Gauss-Kruger CM 135E
    2514, # Pulkovo 1942 / Gauss-Kruger CM 141E
    2515, # Pulkovo 1942 / Gauss-Kruger CM 147E
    2516, # Pulkovo 1942 / Gauss-Kruger CM 153E
    2517, # Pulkovo 1942 / Gauss-Kruger CM 159E
    2518, # Pulkovo 1942 / Gauss-Kruger CM 165E
    2519, # Pulkovo 1942 / Gauss-Kruger CM 171E
    2520, # Pulkovo 1942 / Gauss-Kruger CM 177E
    2521, # Pulkovo 1942 / Gauss-Kruger CM 177W
    2522, # Pulkovo 1942 / Gauss-Kruger CM 171W
    2523, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 7
    2524, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 8
    2525, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 9
    2526, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 10
    2527, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 11
    2528, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 12
    2529, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 13
    2530, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 14
    2531, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 15
    2532, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 16
    2533, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 17
    2534, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 18
    2535, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 19
    2536, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 20
    2537, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 21
    2538, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 22
    2539, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 23
    2540, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 24
    2541, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 25
    2542, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 26
    2543, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 27
    2544, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 28
    2545, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 29
    2546, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 30
    2547, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 31
    2548, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 32
    2549, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 33
    2551, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 34
    2552, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 35
    2553, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 36
    2554, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 37
    2555, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 38
    2556, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 39
    2557, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 40
    2558, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 41
    2559, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 42
    2560, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 43
    2561, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 44
    2562, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 45
    2563, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 46
    2564, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 47
    2565, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 48
    2566, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 49
    2567, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 50
    2568, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 51
    2569, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 52
    2570, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 53
    2571, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 54
    2572, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 55
    2573, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 56
    2574, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 57
    2575, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 58
    2576, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 59
    2577, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 60
    2578, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 61
    2579, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 62
    2580, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 63
    2581, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 64
    2582, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 21E
    2583, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 24E
    2584, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 27E
    2585, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 30E
    2586, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 33E
    2587, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 36E
    2588, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 39E
    2589, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 42E
    2590, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 45E
    2591, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 48E
    2592, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 51E
    2593, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 54E
    2594, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 57E
    2595, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 60E
    2596, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 63E
    2597, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 66E
    2598, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 69E
    2599, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 72E
    2600, # Lietuvos Koordinoei Sistema 1994
    2601, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 75E
    2602, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 78E
    2603, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 81E
    2604, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 84E
    2605, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 87E
    2606, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 90E
    2607, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 93E
    2608, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 96E
    2609, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 99E
    2610, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 102E
    2611, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 105E
    2612, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 108E
    2613, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 111E
    2614, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 114E
    2615, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 117E
    2616, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 120E
    2617, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 123E
    2618, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 126E
    2619, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 129E
    2620, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 132E
    2621, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 135E
    2622, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 138E
    2623, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 141E
    2624, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 144E
    2625, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 147E
    2626, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 150E
    2627, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 153E
    2628, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 156E
    2629, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 159E
    2630, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 162E
    2631, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 165E
    2632, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 168E
    2633, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 171E
    2634, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 174E
    2635, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 177E
    2636, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 180E
    2637, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 177W
    2638, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 174W
    2639, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 171W
    2640, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 168W
    2641, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 7
    2642, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 8
    2643, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 9
    2644, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 10
    2645, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 11
    2646, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 12
    2647, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 13
    2648, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 14
    2649, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 15
    2650, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 16
    2651, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 17
    2652, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 18
    2653, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 19
    2654, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 20
    2655, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 21
    2656, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 22
    2657, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 23
    2658, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 24
    2659, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 25
    2660, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 26
    2661, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 27
    2662, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 28
    2663, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 29
    2664, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 30
    2665, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 31
    2666, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 32
    2667, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 33
    2668, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 34
    2669, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 35
    2670, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 36
    2671, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 37
    2672, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 38
    2673, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 39
    2674, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 40
    2675, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 41
    2676, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 42
    2677, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 43
    2678, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 44
    2679, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 45
    2680, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 46
    2681, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 47
    2682, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 48
    2683, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 49
    2684, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 50
    2685, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 51
    2686, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 52
    2687, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 53
    2688, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 54
    2689, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 55
    2690, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 56
    2691, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 57
    2692, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 58
    2693, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 59
    2694, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 60
    2695, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 61
    2696, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 62
    2697, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 63
    2698, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 64
    2699, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 21E
    2700, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 24E
    2701, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 27E
    2702, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 30E
    2703, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 33E
    2704, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 36E
    2705, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 39E
    2706, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 42E
    2707, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 45E
    2708, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 48E
    2709, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 51E
    2710, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 54E
    2711, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 57E
    2712, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 60E
    2713, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 63E
    2714, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 66E
    2715, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 69E
    2716, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 72E
    2717, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 75E
    2718, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 78E
    2719, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 81E
    2720, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 84E
    2721, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 87E
    2722, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 90E
    2723, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 93E
    2724, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 96E
    2725, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 99E
    2726, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 102E
    2727, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 105E
    2728, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 108E
    2729, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 111E
    2730, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 114E
    2731, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 117E
    2732, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 120E
    2733, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 123E
    2734, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 126E
    2735, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 129E
    2738, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 132E
    2739, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 135E
    2740, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 138E
    2741, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 141E
    2742, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 144E
    2743, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 147E
    2744, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 150E
    2745, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 153E
    2746, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 156E
    2747, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 159E
    2748, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 162E
    2749, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 165E
    2750, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 168E
    2751, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 171E
    2752, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 174E
    2753, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 177E
    2754, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 180E
    2755, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 177W
    2756, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 174W
    2757, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 171W
    2758, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 168W
    2935, # Pulkovo 1942 / CS63 zone A1
    2936, # Pulkovo 1942 / CS63 zone A2
    2937, # Pulkovo 1942 / CS63 zone A3
    2938, # Pulkovo 1942 / CS63 zone A4
    2939, # Pulkovo 1942 / CS63 zone K2
    2940, # Pulkovo 1942 / CS63 zone K3
    2941, # Pulkovo 1942 / CS63 zone K4
    2953, # NAD83(CSRS) / New Brunswick Stereographic
    3006, # SWEREF99 TM
    3007, # SWEREF99 12 00
    3008, # SWEREF99 13 30
    3009, # SWEREF99 15 00
    3010, # SWEREF99 16 30
    3011, # SWEREF99 18 00
    3012, # SWEREF99 14 15
    3013, # SWEREF99 15 45
    3014, # SWEREF99 17 15
    3015, # SWEREF99 18 45
    3016, # SWEREF99 20 15
    3017, # SWEREF99 21 45
    3018, # SWEREF99 23 15
    3019, # RT90 7.5 gon V
    3020, # RT90 5 gon V
    3021, # RT90 2.5 gon V
    3022, # RT90 0 gon
    3023, # RT90 2.5 gon O
    3024, # RT90 5 gon O
    3025, # RT38 7.5 gon V
    3026, # RT38 5 gon V
    3027, # RT38 2.5 gon V
    3028, # RT38 0 gon
    3029, # RT38 2.5 gon O
    3030, # RT38 5 gon O
    3034, # ETRS89 / LCC Europe
    3035, # ETRS89 / LAEA Europe
    3038, # ETRS89 / TM26
    3039, # ETRS89 / TM27
    3040, # ETRS89 / UTM zone 28N (N-E)
    3041, # ETRS89 / UTM zone 29N (N-E)
    3042, # ETRS89 / UTM zone 30N (N-E)
    3043, # ETRS89 / UTM zone 31N (N-E)
    3044, # ETRS89 / UTM zone 32N (N-E)
    3045, # ETRS89 / UTM zone 33N (N-E)
    3046, # ETRS89 / UTM zone 34N (N-E)
    3047, # ETRS89 / UTM zone 35N (N-E)
    3048, # ETRS89 / UTM zone 36N (N-E)
    3049, # ETRS89 / UTM zone 37N (N-E)
    3050, # ETRS89 / TM38
    3051, # ETRS89 / TM39
    3058, # Helle 1954 / Jan Mayen Grid
    3059, # LKS92 / Latvia TM
    3068, # DHDN / Soldner Berlin
    3114, # MAGNA-SIRGAS / Colombia Far West zone
    3115, # MAGNA-SIRGAS / Colombia West zone
    3116, # MAGNA-SIRGAS / Colombia Bogota zone
    3117, # MAGNA-SIRGAS / Colombia East Central zone
    3118, # MAGNA-SIRGAS / Colombia East zone
    3120, # Pulkovo 1942(58) / Poland zone I
    3126, # ETRS89 / ETRS-GK19FIN
    3127, # ETRS89 / ETRS-GK20FIN
    3128, # ETRS89 / ETRS-GK21FIN
    3129, # ETRS89 / ETRS-GK22FIN
    3130, # ETRS89 / ETRS-GK23FIN
    3131, # ETRS89 / ETRS-GK24FIN
    3132, # ETRS89 / ETRS-GK25FIN
    3133, # ETRS89 / ETRS-GK26FIN
    3134, # ETRS89 / ETRS-GK27FIN
    3135, # ETRS89 / ETRS-GK28FIN
    3136, # ETRS89 / ETRS-GK29FIN
    3137, # ETRS89 / ETRS-GK30FIN
    3138, # ETRS89 / ETRS-GK31FIN
    3139, # Vanua Levu 1915 / Vanua Levu Grid
    3140, # Viti Levu 1912 / Viti Levu Grid
    3144, # FD54 / Faroe Lambert
    3145, # ETRS89 / Faroe Lambert
    3146, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 6
    3147, # Pulkovo 1942 / 3-degree Gauss-Kruger CM 18E
    3150, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 6
    3151, # Pulkovo 1995 / 3-degree Gauss-Kruger CM 18E
    3152, # ST74
    3173, # fk89 / Faroe Lambert FK89
    3300, # Estonian Coordinate System of 1992
    3301, # Estonian Coordinate System of 1997
    3328, # Pulkovo 1942(58) / GUGiK-80
    3329, # Pulkovo 1942(58) / 3-degree Gauss-Kruger zone 5
    3330, # Pulkovo 1942(58) / 3-degree Gauss-Kruger zone 6
    3331, # Pulkovo 1942(58) / 3-degree Gauss-Kruger zone 7
    3332, # Pulkovo 1942(58) / 3-degree Gauss-Kruger zone 8
    3333, # Pulkovo 1942(58) / Gauss-Kruger zone 3
    3334, # Pulkovo 1942(58) / Gauss-Kruger zone 4
    3335, # Pulkovo 1942(58) / Gauss-Kruger zone 5
    3346, # LKS94 / Lithuania TM
    3350, # Pulkovo 1942 / CS63 zone C0
    3351, # Pulkovo 1942 / CS63 zone C1
    3352, # Pulkovo 1942 / CS63 zone C2
    3366, # Hong Kong 1963 Grid System
    3386, # KKJ / Finland zone 0
    3387, # KKJ / Finland zone 5
    3388, # Pulkovo 1942 / Caspian Sea Mercator
    3389, # Pulkovo 1942 / 3-degree Gauss-Kruger zone 60
    3390, # Pulkovo 1995 / 3-degree Gauss-Kruger zone 60
    3396, # PD/83 / 3-degree Gauss-Kruger zone 3
    3397, # PD/83 / 3-degree Gauss-Kruger zone 4
    3398, # RD/83 / 3-degree Gauss-Kruger zone 4
    3399, # RD/83 / 3-degree Gauss-Kruger zone 5
    3407, # Hong Kong 1963 Grid System
    3414, # SVY21 / Singapore TM
    3416, # ETRS89 / Austria Lambert
    3764, # NZGD2000 / Chatham Island Circuit 2000
    3788, # NZGD2000 / Auckland Islands TM 2000
    3789, # NZGD2000 / Campbell Island TM 2000
    3790, # NZGD2000 / Antipodes Islands TM 2000
    3791, # NZGD2000 / Raoul Island TM 2000
    3793, # NZGD2000 / Chatham Islands TM 2000
    3795, # NAD27 / Cuba Norte
    3796, # NAD27 / Cuba Sur
    3819, # HD1909
    3821, # TWD67
    3823, # TWD97
    3824, # TWD97
    3833, # Pulkovo 1942(58) / Gauss-Kruger zone 2
    3834, # Pulkovo 1942(83) / Gauss-Kruger zone 2
    3835, # Pulkovo 1942(83) / Gauss-Kruger zone 3
    3836, # Pulkovo 1942(83) / Gauss-Kruger zone 4
    3837, # Pulkovo 1942(58) / 3-degree Gauss-Kruger zone 3
    3838, # Pulkovo 1942(58) / 3-degree Gauss-Kruger zone 4
    3839, # Pulkovo 1942(58) / 3-degree Gauss-Kruger zone 9
    3840, # Pulkovo 1942(58) / 3-degree Gauss-Kruger zone 10
    3841, # Pulkovo 1942(83) / 3-degree Gauss-Kruger zone 6
    3842, # Pulkovo 1942(83) / 3-degree Gauss-Kruger zone 7
    3843, # Pulkovo 1942(83) / 3-degree Gauss-Kruger zone 8
    3844, # Pulkovo 1942(58) / Stereo70
    3845, # SWEREF99 / RT90 7.5 gon V emulation
    3846, # SWEREF99 / RT90 5 gon V emulation
    3847, # SWEREF99 / RT90 2.5 gon V emulation
    3848, # SWEREF99 / RT90 0 gon emulation
    3849, # SWEREF99 / RT90 2.5 gon O emulation
    3850, # SWEREF99 / RT90 5 gon O emulation
    3851, # NZGD2000 / NZCS2000
    3852, # RSRGD2000 / DGLC2000
    3854, # County ST74
    3873, # ETRS89 / GK19FIN
    3874, # ETRS89 / GK20FIN
    3875, # ETRS89 / GK21FIN
    3876, # ETRS89 / GK22FIN
    3877, # ETRS89 / GK23FIN
    3878, # ETRS89 / GK24FIN
    3879, # ETRS89 / GK25FIN
    3880, # ETRS89 / GK26FIN
    3881, # ETRS89 / GK27FIN
    3882, # ETRS89 / GK28FIN
    3883, # ETRS89 / GK29FIN
    3884, # ETRS89 / GK30FIN
    3885, # ETRS89 / GK31FIN
    3888, # IGRS
    3889, # IGRS
    3906, # MGI 1901
    3907, # MGI 1901 / Balkans zone 5
    3908, # MGI 1901 / Balkans zone 6
    3909, # MGI 1901 / Balkans zone 7
    3910, # MGI 1901 / Balkans zone 8
    3911, # MGI 1901 / Slovenia Grid
    4001, # Unknown datum based upon the Airy 1830 ellipsoid
    4002, # Unknown datum based upon the Airy Modified 1849 ellipsoid
    4003, # Unknown datum based upon the Australian National Spheroid
    4004, # Unknown datum based upon the Bessel 1841 ellipsoid
    4005, # Unknown datum based upon the Bessel Modified ellipsoid
    4006, # Unknown datum based upon the Bessel Namibia ellipsoid
    4007, # Unknown datum based upon the Clarke 1858 ellipsoid
    4008, # Unknown datum based upon the Clarke 1866 ellipsoid
    4009, # Unknown datum based upon the Clarke 1866 Michigan ellipsoid
    4010, # Unknown datum based upon the Clarke 1880 (Benoit) ellipsoid
    4011, # Unknown datum based upon the Clarke 1880 (IGN) ellipsoid
    4012, # Unknown datum based upon the Clarke 1880 (RGS) ellipsoid
    4013, # Unknown datum based upon the Clarke 1880 (Arc) ellipsoid
    4014, # Unknown datum based upon the Clarke 1880 (SGA 1922) ellipsoid
    4015, # Unknown datum based upon the Everest 1830 (1937 Adjustment) ellipsoid
    4016, # Unknown datum based upon the Everest 1830 (1967 Definition) ellipsoid
    4017, # MOLDREF99
    4018, # Unknown datum based upon the Everest 1830 Modified ellipsoid
    4019, # Unknown datum based upon the GRS 1980 ellipsoid
    4020, # Unknown datum based upon the Helmert 1906 ellipsoid
    4021, # Unknown datum based upon the Indonesian National Spheroid
    4022, # Unknown datum based upon the International 1924 ellipsoid
    4023, # MOLDREF99
    4024, # Unknown datum based upon the Krassowsky 1940 ellipsoid
    4025, # Unknown datum based upon the NWL 9D ellipsoid
    4026, # MOLDREF99 / Moldova TM
    4027, # Unknown datum based upon the Plessis 1817 ellipsoid
    4028, # Unknown datum based upon the Struve 1860 ellipsoid
    4029, # Unknown datum based upon the War Office ellipsoid
    4030, # Unknown datum based upon the WGS 84 ellipsoid
    4031, # Unknown datum based upon the GEM 10C ellipsoid
    4032, # Unknown datum based upon the OSU86F ellipsoid
    4033, # Unknown datum based upon the OSU91A ellipsoid
    4034, # Unknown datum based upon the Clarke 1880 ellipsoid
    4035, # Unknown datum based upon the Authalic Sphere
    4036, # Unknown datum based upon the GRS 1967 ellipsoid
    4037, # WGS 84 / TMzn35N
    4038, # WGS 84 / TMzn36N
    4040, # RGRDC 2005
    4041, # Unknown datum based upon the Average Terrestrial System 1977 ellipsoid
    4042, # Unknown datum based upon the Everest (1830 Definition) ellipsoid
    4043, # Unknown datum based upon the WGS 72 ellipsoid
    4044, # Unknown datum based upon the Everest 1830 (1962 Definition) ellipsoid
    4045, # Unknown datum based upon the Everest 1830 (1975 Definition) ellipsoid
    4046, # RGRDC 2005
    4047, # Unspecified datum based upon the GRS 1980 Authalic Sphere
    4052, # Unspecified datum based upon the Clarke 1866 Authalic Sphere
    4053, # Unspecified datum based upon the International 1924 Authalic Sphere
    4054, # Unspecified datum based upon the Hughes 1980 ellipsoid
    4055, # Popular Visualisation CRS
    4074, # SREF98
    4075, # SREF98
    4080, # REGCAN95
    4081, # REGCAN95
    4120, # Greek
    4121, # GGRS87
    4122, # ATS77
    4123, # KKJ
    4124, # RT90
    4125, # Samboja
    4126, # LKS94 (ETRS89)
    4127, # Tete
    4128, # Madzansua
    4129, # Observatario
    4130, # Moznet
    4131, # Indian 1960
    4132, # FD58
    4133, # EST92
    4134, # PSD93
    4135, # Old Hawaiian
    4136, # St. Lawrence Island
    4137, # St. Paul Island
    4138, # St. George Island
    4139, # Puerto Rico
    4140, # NAD83(CSRS98)
    4141, # Israel
    4142, # Locodjo 1965
    4143, # Abidjan 1987
    4144, # Kalianpur 1937
    4145, # Kalianpur 1962
    4146, # Kalianpur 1975
    4147, # Hanoi 1972
    4148, # Hartebeesthoek94
    4149, # CH1903
    4150, # CH1903+
    4151, # CHTRF95
    4152, # NAD83(HARN)
    4153, # Rassadiran
    4154, # ED50(ED77)
    4155, # Dabola 1981
    4156, # S-JTSK
    4157, # Mount Dillon
    4158, # Naparima 1955
    4159, # ELD79
    4160, # Chos Malal 1914
    4161, # Pampa del Castillo
    4162, # Korean 1985
    4163, # Yemen NGN96
    4164, # South Yemen
    4165, # Bissau
    4166, # Korean 1995
    4167, # NZGD2000
    4168, # Accra
    4169, # American Samoa 1962
    4170, # SIRGAS 1995
    4171, # RGF93
    4172, # POSGAR
    4173, # IRENET95
    4174, # Sierra Leone 1924
    4175, # Sierra Leone 1968
    4176, # Australian Antarctic
    4178, # Pulkovo 1942(83)
    4179, # Pulkovo 1942(58)
    4180, # EST97
    4181, # Luxembourg 1930
    4182, # Azores Occidental 1939
    4183, # Azores Central 1948
    4184, # Azores Oriental 1940
    4185, # Madeira 1936
    4188, # OSNI 1952
    4189, # REGVEN
    4190, # POSGAR 98
    4191, # Albanian 1987
    4192, # Douala 1948
    4193, # Manoca 1962
    4194, # Qornoq 1927
    4195, # Scoresbysund 1952
    4196, # Ammassalik 1958
    4197, # Garoua
    4198, # Kousseri
    4199, # Egypt 1930
    4200, # Pulkovo 1995
    4201, # Adindan
    4202, # AGD66
    4203, # AGD84
    4204, # Ain el Abd
    4205, # Afgooye
    4206, # Agadez
    4207, # Lisbon
    4208, # Aratu
    4209, # Arc 1950
    4210, # Arc 1960
    4211, # Batavia
    4212, # Barbados 1938
    4213, # Beduaram
    4214, # Beijing 1954
    4215, # Belge 1950
    4216, # Bermuda 1957
    4218, # Bogota 1975
    4219, # Bukit Rimpah
    4220, # Camacupa
    4221, # Campo Inchauspe
    4222, # Cape
    4223, # Carthage
    4224, # Chua
    4225, # Corrego Alegre 1970-72
    4226, # Cote d'Ivoire
    4227, # Deir ez Zor
    4228, # Douala
    4229, # Egypt 1907
    4230, # ED50
    4231, # ED87
    4232, # Fahud
    4233, # Gandajika 1970
    4234, # Garoua
    4235, # Guyane Francaise
    4236, # Hu Tzu Shan 1950
    4237, # HD72
    4238, # ID74
    4239, # Indian 1954
    4240, # Indian 1975
    4241, # Jamaica 1875
    4242, # JAD69
    4243, # Kalianpur 1880
    4244, # Kandawala
    4245, # Kertau 1968
    4246, # KOC
    4247, # La Canoa
    4248, # PSAD56
    4249, # Lake
    4250, # Leigon
    4251, # Liberia 1964
    4252, # Lome
    4253, # Luzon 1911
    4254, # Hito XVIII 1963
    4255, # Herat North
    4256, # Mahe 1971
    4257, # Makassar
    4258, # ETRS89
    4259, # Malongo 1987
    4260, # Manoca
    4261, # Merchich
    4262, # Massawa
    4263, # Minna
    4264, # Mhast
    4265, # Monte Mario
    4266, # M'poraloko
    4267, # NAD27
    4268, # NAD27 Michigan
    4269, # NAD83
    4270, # Nahrwan 1967
    4271, # Naparima 1972
    4272, # NZGD49
    4273, # NGO 1948
    4274, # Datum 73
    4275, # NTF
    4276, # NSWC 9Z-2
    4277, # OSGB 1936
    4278, # OSGB70
    4279, # OS(SN)80
    4280, # Padang
    4281, # Palestine 1923
    4282, # Pointe Noire
    4283, # GDA94
    4284, # Pulkovo 1942
    4285, # Qatar 1974
    4286, # Qatar 1948
    4287, # Qornoq
    4288, # Loma Quintana
    4289, # Amersfoort
    4291, # SAD69
    4292, # Sapper Hill 1943
    4293, # Schwarzeck
    4294, # Segora
    4295, # Serindung
    4296, # Sudan
    4297, # Tananarive
    4298, # Timbalai 1948
    4299, # TM65
    4300, # TM75
    4301, # Tokyo
    4302, # Trinidad 1903
    4303, # TC(1948)
    4304, # Voirol 1875
    4306, # Bern 1938
    4307, # Nord Sahara 1959
    4308, # RT38
    4309, # Yacare
    4310, # Yoff
    4311, # Zanderij
    4312, # MGI
    4313, # Belge 1972
    4314, # DHDN
    4315, # Conakry 1905
    4316, # Dealul Piscului 1930
    4317, # Dealul Piscului 1970
    4318, # NGN
    4319, # KUDAMS
    4322, # WGS 72
    4324, # WGS 72BE
    4326, # WGS 84
    4327, # WGS 84 (geographic 3D)
    4329, # WGS 84 (3D)
    4339, # Australian Antarctic (3D)
    4341, # EST97 (3D)
    4343, # CHTRF95 (3D)
    4345, # ETRS89 (3D)
    4347, # GDA94 (3D)
    4349, # Hartebeesthoek94 (3D)
    4351, # IRENET95 (3D)
    4353, # JGD2000 (3D)
    4355, # LKS94 (ETRS89) (3D)
    4357, # Moznet (3D)
    4359, # NAD83(CSRS) (3D)
    4361, # NAD83(HARN) (3D)
    4363, # NZGD2000 (3D)
    4365, # POSGAR 98 (3D)
    4367, # REGVEN (3D)
    4369, # RGF93 (3D)
    4371, # RGFG95 (3D)
    4373, # RGR92 (3D)
    4375, # SIRGAS (3D)
    4377, # SWEREF99 (3D)
    4379, # Yemen NGN96 (3D)
    4381, # RGNC 1991 (3D)
    4383, # RRAF 1991 (3D)
    4386, # ISN93 (3D)
    4388, # LKS92 (3D)
    4417, # Pulkovo 1942(83) / 3-degree Gauss-Kruger zone 7
    4434, # Pulkovo 1942(83) / 3-degree Gauss-Kruger zone 8
    4463, # RGSPM06
    4466, # RGSPM06
    4469, # RGM04
    4470, # RGM04
    4472, # Cadastre 1997
    4475, # Cadastre 1997
    4480, # China Geodetic Coordinate System 2000
    4482, # Mexican Datum of 1993
    4483, # Mexican Datum of 1993
    4490, # China Geodetic Coordinate System 2000
    4491, # CGCS2000 / Gauss-Kruger zone 13
    4492, # CGCS2000 / Gauss-Kruger zone 14
    4493, # CGCS2000 / Gauss-Kruger zone 15
    4494, # CGCS2000 / Gauss-Kruger zone 16
    4495, # CGCS2000 / Gauss-Kruger zone 17
    4496, # CGCS2000 / Gauss-Kruger zone 18
    4497, # CGCS2000 / Gauss-Kruger zone 19
    4498, # CGCS2000 / Gauss-Kruger zone 20
    4499, # CGCS2000 / Gauss-Kruger zone 21
    4500, # CGCS2000 / Gauss-Kruger zone 22
    4501, # CGCS2000 / Gauss-Kruger zone 23
    4502, # CGCS2000 / Gauss-Kruger CM 75E
    4503, # CGCS2000 / Gauss-Kruger CM 81E
    4504, # CGCS2000 / Gauss-Kruger CM 87E
    4505, # CGCS2000 / Gauss-Kruger CM 93E
    4506, # CGCS2000 / Gauss-Kruger CM 99E
    4507, # CGCS2000 / Gauss-Kruger CM 105E
    4508, # CGCS2000 / Gauss-Kruger CM 111E
    4509, # CGCS2000 / Gauss-Kruger CM 117E
    4510, # CGCS2000 / Gauss-Kruger CM 123E
    4511, # CGCS2000 / Gauss-Kruger CM 129E
    4512, # CGCS2000 / Gauss-Kruger CM 135E
    4513, # CGCS2000 / 3-degree Gauss-Kruger zone 25
    4514, # CGCS2000 / 3-degree Gauss-Kruger zone 26
    4515, # CGCS2000 / 3-degree Gauss-Kruger zone 27
    4516, # CGCS2000 / 3-degree Gauss-Kruger zone 28
    4517, # CGCS2000 / 3-degree Gauss-Kruger zone 29
    4518, # CGCS2000 / 3-degree Gauss-Kruger zone 30
    4519, # CGCS2000 / 3-degree Gauss-Kruger zone 31
    4520, # CGCS2000 / 3-degree Gauss-Kruger zone 32
    4521, # CGCS2000 / 3-degree Gauss-Kruger zone 33
    4522, # CGCS2000 / 3-degree Gauss-Kruger zone 34
    4523, # CGCS2000 / 3-degree Gauss-Kruger zone 35
    4524, # CGCS2000 / 3-degree Gauss-Kruger zone 36
    4525, # CGCS2000 / 3-degree Gauss-Kruger zone 37
    4526, # CGCS2000 / 3-degree Gauss-Kruger zone 38
    4527, # CGCS2000 / 3-degree Gauss-Kruger zone 39
    4528, # CGCS2000 / 3-degree Gauss-Kruger zone 40
    4529, # CGCS2000 / 3-degree Gauss-Kruger zone 41
    4530, # CGCS2000 / 3-degree Gauss-Kruger zone 42
    4531, # CGCS2000 / 3-degree Gauss-Kruger zone 43
    4532, # CGCS2000 / 3-degree Gauss-Kruger zone 44
    4533, # CGCS2000 / 3-degree Gauss-Kruger zone 45
    4534, # CGCS2000 / 3-degree Gauss-Kruger CM 75E
    4535, # CGCS2000 / 3-degree Gauss-Kruger CM 78E
    4536, # CGCS2000 / 3-degree Gauss-Kruger CM 81E
    4537, # CGCS2000 / 3-degree Gauss-Kruger CM 84E
    4538, # CGCS2000 / 3-degree Gauss-Kruger CM 87E
    4539, # CGCS2000 / 3-degree Gauss-Kruger CM 90E
    4540, # CGCS2000 / 3-degree Gauss-Kruger CM 93E
    4541, # CGCS2000 / 3-degree Gauss-Kruger CM 96E
    4542, # CGCS2000 / 3-degree Gauss-Kruger CM 99E
    4543, # CGCS2000 / 3-degree Gauss-Kruger CM 102E
    4544, # CGCS2000 / 3-degree Gauss-Kruger CM 105E
    4545, # CGCS2000 / 3-degree Gauss-Kruger CM 108E
    4546, # CGCS2000 / 3-degree Gauss-Kruger CM 111E
    4547, # CGCS2000 / 3-degree Gauss-Kruger CM 114E
    4548, # CGCS2000 / 3-degree Gauss-Kruger CM 117E
    4549, # CGCS2000 / 3-degree Gauss-Kruger CM 120E
    4550, # CGCS2000 / 3-degree Gauss-Kruger CM 123E
    4551, # CGCS2000 / 3-degree Gauss-Kruger CM 126E
    4552, # CGCS2000 / 3-degree Gauss-Kruger CM 129E
    4553, # CGCS2000 / 3-degree Gauss-Kruger CM 132E
    4554, # CGCS2000 / 3-degree Gauss-Kruger CM 135E
    4555, # New Beijing
    4557, # RRAF 1991
    4558, # RRAF 1991
    4568, # New Beijing / Gauss-Kruger zone 13
    4569, # New Beijing / Gauss-Kruger zone 14
    4570, # New Beijing / Gauss-Kruger zone 15
    4571, # New Beijing / Gauss-Kruger zone 16
    4572, # New Beijing / Gauss-Kruger zone 17
    4573, # New Beijing / Gauss-Kruger zone 18
    4574, # New Beijing / Gauss-Kruger zone 19
    4575, # New Beijing / Gauss-Kruger zone 20
    4576, # New Beijing / Gauss-Kruger zone 21
    4577, # New Beijing / Gauss-Kruger zone 22
    4578, # New Beijing / Gauss-Kruger zone 23
    4579, # New Beijing / Gauss-Kruger CM 75E
    4580, # New Beijing / Gauss-Kruger CM 81E
    4581, # New Beijing / Gauss-Kruger CM 87E
    4582, # New Beijing / Gauss-Kruger CM 93E
    4583, # New Beijing / Gauss-Kruger CM 99E
    4584, # New Beijing / Gauss-Kruger CM 105E
    4585, # New Beijing / Gauss-Kruger CM 111E
    4586, # New Beijing / Gauss-Kruger CM 117E
    4587, # New Beijing / Gauss-Kruger CM 123E
    4588, # New Beijing / Gauss-Kruger CM 129E
    4589, # New Beijing / Gauss-Kruger CM 135E
    4600, # Anguilla 1957
    4601, # Antigua 1943
    4602, # Dominica 1945
    4603, # Grenada 1953
    4604, # Montserrat 1958
    4605, # St. Kitts 1955
    4606, # St. Lucia 1955
    4607, # St. Vincent 1945
    4608, # NAD27(76)
    4609, # NAD27(CGQ77)
    4610, # Xian 1980
    4611, # Hong Kong 1980
    4612, # JGD2000
    4613, # Segara
    4614, # QND95
    4615, # Porto Santo
    4616, # Selvagem Grande
    4617, # NAD83(CSRS)
    4618, # SAD69
    4619, # SWEREF99
    4620, # Point 58
    4621, # Fort Marigot
    4622, # Guadeloupe 1948
    4623, # CSG67
    4624, # RGFG95
    4625, # Martinique 1938
    4626, # Reunion 1947
    4627, # RGR92
    4628, # Tahiti 52
    4629, # Tahaa 54
    4630, # IGN72 Nuku Hiva
    4631, # K0 1949
    4632, # Combani 1950
    4633, # IGN56 Lifou
    4634, # IGN72 Grand Terre
    4635, # ST87 Ouvea
    4636, # Petrels 1972
    4637, # Perroud 1950
    4638, # Saint Pierre et Miquelon 1950
    4639, # MOP78
    4640, # RRAF 1991
    4641, # IGN53 Mare
    4642, # ST84 Ile des Pins
    4643, # ST71 Belep
    4644, # NEA74 Noumea
    4645, # RGNC 1991
    4646, # Grand Comoros
    4652, # New Beijing / 3-degree Gauss-Kruger zone 25
    4653, # New Beijing / 3-degree Gauss-Kruger zone 26
    4654, # New Beijing / 3-degree Gauss-Kruger zone 27
    4655, # New Beijing / 3-degree Gauss-Kruger zone 28
    4656, # New Beijing / 3-degree Gauss-Kruger zone 29
    4657, # Reykjavik 1900
    4658, # Hjorsey 1955
    4659, # ISN93
    4660, # Helle 1954
    4661, # LKS92
    4662, # IGN72 Grande Terre
    4663, # Porto Santo 1995
    4664, # Azores Oriental 1995
    4665, # Azores Central 1995
    4666, # Lisbon 1890
    4667, # IKBD-92
    4668, # ED79
    4669, # LKS94
    4670, # IGM95
    4671, # Voirol 1879
    4672, # Chatham Islands 1971
    4673, # Chatham Islands 1979
    4674, # SIRGAS 2000
    4675, # Guam 1963
    4676, # Vientiane 1982
    4677, # Lao 1993
    4678, # Lao 1997
    4679, # Jouik 1961
    4680, # Nouakchott 1965
    4681, # Mauritania 1999
    4682, # Gulshan 303
    4683, # PRS92
    4684, # Gan 1970
    4685, # Gandajika
    4686, # MAGNA-SIRGAS
    4687, # RGPF
    4688, # Fatu Iva 72
    4689, # IGN63 Hiva Oa
    4690, # Tahiti 79
    4691, # Moorea 87
    4692, # Maupiti 83
    4693, # Nakhl-e Ghanem
    4694, # POSGAR 94
    4695, # Katanga 1955
    4696, # Kasai 1953
    4697, # IGC 1962 6th Parallel South
    4698, # IGN 1962 Kerguelen
    4699, # Le Pouce 1934
    4700, # IGN Astro 1960
    4701, # IGCB 1955
    4702, # Mauritania 1999
    4703, # Mhast 1951
    4704, # Mhast (onshore)
    4705, # Mhast (offshore)
    4706, # Egypt Gulf of Suez S-650 TL
    4707, # Tern Island 1961
    4708, # Cocos Islands 1965
    4709, # Iwo Jima 1945
    4710, # St. Helena 1971
    4711, # Marcus Island 1952
    4712, # Ascension Island 1958
    4713, # Ayabelle Lighthouse
    4714, # Bellevue
    4715, # Camp Area Astro
    4716, # Phoenix Islands 1966
    4717, # Cape Canaveral
    4718, # Solomon 1968
    4719, # Easter Island 1967
    4720, # Fiji 1986
    4721, # Fiji 1956
    4722, # South Georgia 1968
    4723, # GCGD59
    4724, # Diego Garcia 1969
    4725, # Johnston Island 1961
    4726, # SIGD61
    4727, # Midway 1961
    4728, # Pico de las Nieves 1984
    4729, # Pitcairn 1967
    4730, # Santo 1965
    4731, # Viti Levu 1916
    4732, # Marshall Islands 1960
    4733, # Wake Island 1952
    4734, # Tristan 1968
    4735, # Kusaie 1951
    4736, # Deception Island
    4737, # Korea 2000
    4738, # Hong Kong 1963
    4739, # Hong Kong 1963(67)
    4740, # PZ-90
    4741, # FD54
    4742, # GDM2000
    4743, # Karbala 1979
    4744, # Nahrwan 1934
    4745, # RD/83
    4746, # PD/83
    4747, # GR96
    4748, # Vanua Levu 1915
    4749, # RGNC91-93
    4750, # ST87 Ouvea
    4751, # Kertau (RSO)
    4752, # Viti Levu 1912
    4753, # fk89
    4754, # LGD2006
    4755, # DGN95
    4756, # VN-2000
    4757, # SVY21
    4758, # JAD2001
    4759, # NAD83(NSRS2007)
    4760, # WGS 66
    4761, # HTRS96
    4762, # BDA2000
    4763, # Pitcairn 2006
    4764, # RSRGD2000
    4765, # Slovenia 1996
    4766, # New Beijing / 3-degree Gauss-Kruger zone 30
    4767, # New Beijing / 3-degree Gauss-Kruger zone 31
    4768, # New Beijing / 3-degree Gauss-Kruger zone 32
    4769, # New Beijing / 3-degree Gauss-Kruger zone 33
    4770, # New Beijing / 3-degree Gauss-Kruger zone 34
    4771, # New Beijing / 3-degree Gauss-Kruger zone 35
    4772, # New Beijing / 3-degree Gauss-Kruger zone 36
    4773, # New Beijing / 3-degree Gauss-Kruger zone 37
    4774, # New Beijing / 3-degree Gauss-Kruger zone 38
    4775, # New Beijing / 3-degree Gauss-Kruger zone 39
    4776, # New Beijing / 3-degree Gauss-Kruger zone 40
    4777, # New Beijing / 3-degree Gauss-Kruger zone 41
    4778, # New Beijing / 3-degree Gauss-Kruger zone 42
    4779, # New Beijing / 3-degree Gauss-Kruger zone 43
    4780, # New Beijing / 3-degree Gauss-Kruger zone 44
    4781, # New Beijing / 3-degree Gauss-Kruger zone 45
    4782, # New Beijing / 3-degree Gauss-Kruger CM 75E
    4783, # New Beijing / 3-degree Gauss-Kruger CM 78E
    4784, # New Beijing / 3-degree Gauss-Kruger CM 81E
    4785, # New Beijing / 3-degree Gauss-Kruger CM 84E
    4786, # New Beijing / 3-degree Gauss-Kruger CM 87E
    4787, # New Beijing / 3-degree Gauss-Kruger CM 90E
    4788, # New Beijing / 3-degree Gauss-Kruger CM 93E
    4789, # New Beijing / 3-degree Gauss-Kruger CM 96E
    4790, # New Beijing / 3-degree Gauss-Kruger CM 99E
    4791, # New Beijing / 3-degree Gauss-Kruger CM 102E
    4792, # New Beijing / 3-degree Gauss-Kruger CM 105E
    4793, # New Beijing / 3-degree Gauss-Kruger CM 108E
    4794, # New Beijing / 3-degree Gauss-Kruger CM 111E
    4795, # New Beijing / 3-degree Gauss-Kruger CM 114E
    4796, # New Beijing / 3-degree Gauss-Kruger CM 117E
    4797, # New Beijing / 3-degree Gauss-Kruger CM 120E
    4798, # New Beijing / 3-degree Gauss-Kruger CM 123E
    4799, # New Beijing / 3-degree Gauss-Kruger CM 126E
    4800, # New Beijing / 3-degree Gauss-Kruger CM 129E
    4801, # Bern 1898 (Bern)
    4802, # Bogota 1975 (Bogota)
    4803, # Lisbon (Lisbon)
    4804, # Makassar (Jakarta)
    4805, # MGI (Ferro)
    4806, # Monte Mario (Rome)
    4807, # NTF (Paris)
    4808, # Padang (Jakarta)
    4809, # Belge 1950 (Brussels)
    4810, # Tananarive (Paris)
    4811, # Voirol 1875 (Paris)
    4812, # New Beijing / 3-degree Gauss-Kruger CM 132E
    4813, # Batavia (Jakarta)
    4814, # RT38 (Stockholm)
    4815, # Greek (Athens)
    4816, # Carthage (Paris)
    4817, # NGO 1948 (Oslo)
    4818, # S-JTSK (Ferro)
    4819, # Nord Sahara 1959 (Paris)
    4820, # Segara (Jakarta)
    4821, # Voirol 1879 (Paris)
    4822, # New Beijing / 3-degree Gauss-Kruger CM 135E
    4823, # Sao Tome
    4824, # Principe
    4839, # ETRS89 / LCC Germany (N-E)
    4855, # ETRS89 / NTM zone 5
    4856, # ETRS89 / NTM zone 6
    4857, # ETRS89 / NTM zone 7
    4858, # ETRS89 / NTM zone 8
    4859, # ETRS89 / NTM zone 9
    4860, # ETRS89 / NTM zone 10
    4861, # ETRS89 / NTM zone 11
    4862, # ETRS89 / NTM zone 12
    4863, # ETRS89 / NTM zone 13
    4864, # ETRS89 / NTM zone 14
    4865, # ETRS89 / NTM zone 15
    4866, # ETRS89 / NTM zone 16
    4867, # ETRS89 / NTM zone 17
    4868, # ETRS89 / NTM zone 18
    4869, # ETRS89 / NTM zone 19
    4870, # ETRS89 / NTM zone 20
    4871, # ETRS89 / NTM zone 21
    4872, # ETRS89 / NTM zone 22
    4873, # ETRS89 / NTM zone 23
    4874, # ETRS89 / NTM zone 24
    4875, # ETRS89 / NTM zone 25
    4876, # ETRS89 / NTM zone 26
    4877, # ETRS89 / NTM zone 27
    4878, # ETRS89 / NTM zone 28
    4879, # ETRS89 / NTM zone 29
    4880, # ETRS89 / NTM zone 30
    4883, # Slovenia 1996
    4885, # RSRGD2000
    4887, # BDA2000
    4889, # HTRS96
    4891, # WGS 66
    4893, # NAD83(NSRS2007)
    4895, # JAD2001
    4898, # DGN95
    4900, # LGD2006
    4901, # ATF (Paris)
    4902, # NDG (Paris)
    4903, # Madrid 1870 (Madrid)
    4904, # Lisbon 1890 (Lisbon)
    4907, # RGNC91-93
    4909, # GR96
    4921, # GDM2000
    4923, # PZ-90
    4925, # Mauritania 1999
    4927, # Korea 2000
    4929, # POSGAR 94
    4931, # Australian Antarctic
    4933, # CHTRF95
    4935, # EST97
    4937, # ETRS89
    4939, # GDA94
    4941, # Hartebeesthoek94
    4943, # IRENET95
    4945, # ISN93
    4947, # JGD2000
    4949, # LKS92
    4951, # LKS94
    4953, # Moznet
    4955, # NAD83(CSRS)
    4957, # NAD83(HARN)
    4959, # NZGD2000
    4961, # POSGAR 98
    4963, # REGVEN
    4965, # RGF93
    4967, # RGFG95
    4969, # RGNC 1991
    4971, # RGR92
    4973, # RRAF 1991
    4975, # SIRGAS 1995
    4977, # SWEREF99
    4979, # WGS 84
    4981, # Yemen NGN96
    4983, # IGM95
    4985, # WGS 72
    4987, # WGS 72BE
    4989, # SIRGAS 2000
    4991, # Lao 1993
    4993, # Lao 1997
    4995, # PRS92
    4997, # MAGNA-SIRGAS
    4999, # RGPF
    5012, # PTRA08
    5013, # PTRA08
    5048, # ETRS89 / TM35FIN(N,E)
    5105, # ETRS89 / NTM zone 5
    5106, # ETRS89 / NTM zone 6
    5107, # ETRS89 / NTM zone 7
    5108, # ETRS89 / NTM zone 8
    5109, # ETRS89 / NTM zone 9
    5110, # ETRS89 / NTM zone 10
    5111, # ETRS89 / NTM zone 11
    5112, # ETRS89 / NTM zone 12
    5113, # ETRS89 / NTM zone 13
    5114, # ETRS89 / NTM zone 14
    5115, # ETRS89 / NTM zone 15
    5116, # ETRS89 / NTM zone 16
    5117, # ETRS89 / NTM zone 17
    5118, # ETRS89 / NTM zone 18
    5119, # ETRS89 / NTM zone 19
    5120, # ETRS89 / NTM zone 20
    5121, # ETRS89 / NTM zone 21
    5122, # ETRS89 / NTM zone 22
    5123, # ETRS89 / NTM zone 23
    5124, # ETRS89 / NTM zone 24
    5125, # ETRS89 / NTM zone 25
    5126, # ETRS89 / NTM zone 26
    5127, # ETRS89 / NTM zone 27
    5128, # ETRS89 / NTM zone 28
    5129, # ETRS89 / NTM zone 29
    5130, # ETRS89 / NTM zone 30
    5132, # Tokyo 1892
    5167, # Korean 1985 / East Sea Belt
    5168, # Korean 1985 / Central Belt Jeju
    5169, # Tokyo 1892 / Korea West Belt
    5170, # Tokyo 1892 / Korea Central Belt
    5171, # Tokyo 1892 / Korea East Belt
    5172, # Tokyo 1892 / Korea East Sea Belt
    5173, # Korean 1985 / Modified West Belt
    5174, # Korean 1985 / Modified Central Belt
    5175, # Korean 1985 / Modified Central Belt Jeju
    5176, # Korean 1985 / Modified East Belt
    5177, # Korean 1985 / Modified East Sea Belt
    5178, # Korean 1985 / Unified CS
    5179, # Korea 2000 / Unified CS
    5180, # Korea 2000 / West Belt
    5181, # Korea 2000 / Central Belt
    5182, # Korea 2000 / Central Belt Jeju
    5183, # Korea 2000 / East Belt
    5184, # Korea 2000 / East Sea Belt
    5185, # Korea 2000 / West Belt 2010
    5186, # Korea 2000 / Central Belt 2010
    5187, # Korea 2000 / East Belt 2010
    5188, # Korea 2000 / East Sea Belt 2010
    5228, # S-JTSK/05
    5229, # S-JTSK/05 (Ferro)
    5233, # SLD99
    5245, # GDBD2009
    5246, # GDBD2009
    5251, # TUREF
    5252, # TUREF
    5253, # TUREF / TM27
    5254, # TUREF / TM30
    5255, # TUREF / TM33
    5256, # TUREF / TM36
    5257, # TUREF / TM39
    5258, # TUREF / TM42
    5259, # TUREF / TM45
    5263, # DRUKREF 03
    5264, # DRUKREF 03
    5269, # TUREF / 3-degree Gauss-Kruger zone 9
    5270, # TUREF / 3-degree Gauss-Kruger zone 10
    5271, # TUREF / 3-degree Gauss-Kruger zone 11
    5272, # TUREF / 3-degree Gauss-Kruger zone 12
    5273, # TUREF / 3-degree Gauss-Kruger zone 13
    5274, # TUREF / 3-degree Gauss-Kruger zone 14
    5275, # TUREF / 3-degree Gauss-Kruger zone 15
    5323, # ISN2004
    5324, # ISN2004
    5340, # POSGAR 2007
    5342, # POSGAR 2007
    5343, # POSGAR 2007 / Argentina 1
    5344, # POSGAR 2007 / Argentina 2
    5345, # POSGAR 2007 / Argentina 3
    5346, # POSGAR 2007 / Argentina 4
    5347, # POSGAR 2007 / Argentina 5
    5348, # POSGAR 2007 / Argentina 6
    5349, # POSGAR 2007 / Argentina 7
    5353, # MARGEN
    5354, # MARGEN
    5359, # SIRGAS-Chile
    5360, # SIRGAS-Chile
    5364, # CR05
    5365, # CR05
    5367, # CR05 / CRTM05
    5370, # MACARIO SOLIS
    5371, # MACARIO SOLIS
    5372, # Peru96
    5373, # Peru96
    5380, # SIRGAS-ROU98
    5381, # SIRGAS-ROU98
    5392, # SIRGAS_ES2007.8
    5393, # SIRGAS_ES2007.8
    5451, # Ocotepeque 1935
    5464, # Sibun Gorge 1922
    5467, # Panama-Colon 1911
    5479, # RSRGD2000 / MSLC2000
    5480, # RSRGD2000 / BCLC2000
    5481, # RSRGD2000 / PCLC2000
    5482, # RSRGD2000 / RSPS2000
    5488, # RGAF09
    5489, # RGAF09
    5518, # CI1971 / Chatham Islands Map Grid
    5519, # CI1979 / Chatham Islands Map Grid
    5520, # DHDN / 3-degree Gauss-Kruger zone 1
    5524, # Corrego Alegre 1961
    5527, # SAD69(96)
    5545, # PNG94
    5546, # PNG94
    5560, # UCS-2000
    5561, # UCS-2000
    5562, # UCS-2000 / Gauss-Kruger zone 4
    5563, # UCS-2000 / Gauss-Kruger zone 5
    5564, # UCS-2000 / Gauss-Kruger zone 6
    5565, # UCS-2000 / Gauss-Kruger zone 7
    5566, # UCS-2000 / Gauss-Kruger CM 21E
    5567, # UCS-2000 / Gauss-Kruger CM 27E
    5568, # UCS-2000 / Gauss-Kruger CM 33E
    5569, # UCS-2000 / Gauss-Kruger CM 39E
    5570, # UCS-2000 / 3-degree Gauss-Kruger zone 7
    5571, # UCS-2000 / 3-degree Gauss-Kruger zone 8
    5572, # UCS-2000 / 3-degree Gauss-Kruger zone 9
    5573, # UCS-2000 / 3-degree Gauss-Kruger zone 10
    5574, # UCS-2000 / 3-degree Gauss-Kruger zone 11
    5575, # UCS-2000 / 3-degree Gauss-Kruger zone 12
    5576, # UCS-2000 / 3-degree Gauss-Kruger zone 13
    5577, # UCS-2000 / 3-degree Gauss-Kruger CM 21E
    5578, # UCS-2000 / 3-degree Gauss-Kruger CM 24E
    5579, # UCS-2000 / 3-degree Gauss-Kruger CM 27E
    5580, # UCS-2000 / 3-degree Gauss-Kruger CM 30E
    5581, # UCS-2000 / 3-degree Gauss-Kruger CM 33E
    5582, # UCS-2000 / 3-degree Gauss-Kruger CM 36E
    5583, # UCS-2000 / 3-degree Gauss-Kruger CM 39E
    5588, # NAD27 / New Brunswick Stereographic (NAD27)
    5592, # FEH2010
    5593, # FEH2010
    5632, # PTRA08 / LCC Europe
    5633, # PTRA08 / LAEA Europe
    5634, # REGCAN95 / LCC Europe
    5635, # REGCAN95 / LAEA Europe
    5636, # TUREF / LAEA Europe
    5637, # TUREF / LCC Europe
    5638, # ISN2004 / LAEA Europe
    5639, # ISN2004 / LCC Europe
    5651, # ETRS89 / UTM zone 31N (N-zE)
    5652, # ETRS89 / UTM zone 32N (N-zE)
    5653, # ETRS89 / UTM zone 33N (N-zE)
    5681, # DB_REF
    5800, # Astra Minas Grid
    5801, # Barcelona Grid B1
    5802, # Barcelona Grid B2
    5803, # Maturin Grid
    5808, # Maracaibo Cross Grid M4
    5809, # Maracaibo Cross Grid M5
    5810, # La Rosa Grid
    5811, # Mene Grande
    5812, # El Cubo
    5813, # Dabajuro
    5814, # Tucupita
    5815, # Santa Maria de Ipire
    5816, # Barinas west base
    5830, # DB_REF
    5885, # TGD2005
    5886, # TGD2005
    6134, # CIGD11
    6135, # CIGD11
    20004, # Pulkovo 1995 / Gauss-Kruger zone 4
    20005, # Pulkovo 1995 / Gauss-Kruger zone 5
    20006, # Pulkovo 1995 / Gauss-Kruger zone 6
    20007, # Pulkovo 1995 / Gauss-Kruger zone 7
    20008, # Pulkovo 1995 / Gauss-Kruger zone 8
    20009, # Pulkovo 1995 / Gauss-Kruger zone 9
    20010, # Pulkovo 1995 / Gauss-Kruger zone 10
    20011, # Pulkovo 1995 / Gauss-Kruger zone 11
    20012, # Pulkovo 1995 / Gauss-Kruger zone 12
    20013, # Pulkovo 1995 / Gauss-Kruger zone 13
    20014, # Pulkovo 1995 / Gauss-Kruger zone 14
    20015, # Pulkovo 1995 / Gauss-Kruger zone 15
    20016, # Pulkovo 1995 / Gauss-Kruger zone 16
    20017, # Pulkovo 1995 / Gauss-Kruger zone 17
    20018, # Pulkovo 1995 / Gauss-Kruger zone 18
    20019, # Pulkovo 1995 / Gauss-Kruger zone 19
    20020, # Pulkovo 1995 / Gauss-Kruger zone 20
    20021, # Pulkovo 1995 / Gauss-Kruger zone 21
    20022, # Pulkovo 1995 / Gauss-Kruger zone 22
    20023, # Pulkovo 1995 / Gauss-Kruger zone 23
    20024, # Pulkovo 1995 / Gauss-Kruger zone 24
    20025, # Pulkovo 1995 / Gauss-Kruger zone 25
    20026, # Pulkovo 1995 / Gauss-Kruger zone 26
    20027, # Pulkovo 1995 / Gauss-Kruger zone 27
    20028, # Pulkovo 1995 / Gauss-Kruger zone 28
    20029, # Pulkovo 1995 / Gauss-Kruger zone 29
    20030, # Pulkovo 1995 / Gauss-Kruger zone 30
    20031, # Pulkovo 1995 / Gauss-Kruger zone 31
    20032, # Pulkovo 1995 / Gauss-Kruger zone 32
    20064, # Pulkovo 1995 / Gauss-Kruger 4N
    20065, # Pulkovo 1995 / Gauss-Kruger 5N
    20066, # Pulkovo 1995 / Gauss-Kruger 6N
    20067, # Pulkovo 1995 / Gauss-Kruger 7N
    20068, # Pulkovo 1995 / Gauss-Kruger 8N
    20069, # Pulkovo 1995 / Gauss-Kruger 9N
    20070, # Pulkovo 1995 / Gauss-Kruger 10N
    20071, # Pulkovo 1995 / Gauss-Kruger 11N
    20072, # Pulkovo 1995 / Gauss-Kruger 12N
    20073, # Pulkovo 1995 / Gauss-Kruger 13N
    20074, # Pulkovo 1995 / Gauss-Kruger 14N
    20075, # Pulkovo 1995 / Gauss-Kruger 15N
    20076, # Pulkovo 1995 / Gauss-Kruger 16N
    20077, # Pulkovo 1995 / Gauss-Kruger 17N
    20078, # Pulkovo 1995 / Gauss-Kruger 18N
    20079, # Pulkovo 1995 / Gauss-Kruger 19N
    20080, # Pulkovo 1995 / Gauss-Kruger 20N
    20081, # Pulkovo 1995 / Gauss-Kruger 21N
    20082, # Pulkovo 1995 / Gauss-Kruger 22N
    20083, # Pulkovo 1995 / Gauss-Kruger 23N
    20084, # Pulkovo 1995 / Gauss-Kruger 24N
    20085, # Pulkovo 1995 / Gauss-Kruger 25N
    20086, # Pulkovo 1995 / Gauss-Kruger 26N
    20087, # Pulkovo 1995 / Gauss-Kruger 27N
    20088, # Pulkovo 1995 / Gauss-Kruger 28N
    20089, # Pulkovo 1995 / Gauss-Kruger 29N
    20090, # Pulkovo 1995 / Gauss-Kruger 30N
    20091, # Pulkovo 1995 / Gauss-Kruger 31N
    20092, # Pulkovo 1995 / Gauss-Kruger 32N
    21413, # Beijing 1954 / Gauss-Kruger zone 13
    21414, # Beijing 1954 / Gauss-Kruger zone 14
    21415, # Beijing 1954 / Gauss-Kruger zone 15
    21416, # Beijing 1954 / Gauss-Kruger zone 16
    21417, # Beijing 1954 / Gauss-Kruger zone 17
    21418, # Beijing 1954 / Gauss-Kruger zone 18
    21419, # Beijing 1954 / Gauss-Kruger zone 19
    21420, # Beijing 1954 / Gauss-Kruger zone 20
    21421, # Beijing 1954 / Gauss-Kruger zone 21
    21422, # Beijing 1954 / Gauss-Kruger zone 22
    21423, # Beijing 1954 / Gauss-Kruger zone 23
    21453, # Beijing 1954 / Gauss-Kruger CM 75E
    21454, # Beijing 1954 / Gauss-Kruger CM 81E
    21455, # Beijing 1954 / Gauss-Kruger CM 87E
    21456, # Beijing 1954 / Gauss-Kruger CM 93E
    21457, # Beijing 1954 / Gauss-Kruger CM 99E
    21458, # Beijing 1954 / Gauss-Kruger CM 105E
    21459, # Beijing 1954 / Gauss-Kruger CM 111E
    21460, # Beijing 1954 / Gauss-Kruger CM 117E
    21461, # Beijing 1954 / Gauss-Kruger CM 123E
    21462, # Beijing 1954 / Gauss-Kruger CM 129E
    21463, # Beijing 1954 / Gauss-Kruger CM 135E
    21473, # Beijing 1954 / Gauss-Kruger 13N
    21474, # Beijing 1954 / Gauss-Kruger 14N
    21475, # Beijing 1954 / Gauss-Kruger 15N
    21476, # Beijing 1954 / Gauss-Kruger 16N
    21477, # Beijing 1954 / Gauss-Kruger 17N
    21478, # Beijing 1954 / Gauss-Kruger 18N
    21479, # Beijing 1954 / Gauss-Kruger 19N
    21480, # Beijing 1954 / Gauss-Kruger 20N
    21481, # Beijing 1954 / Gauss-Kruger 21N
    21482, # Beijing 1954 / Gauss-Kruger 22N
    21483, # Beijing 1954 / Gauss-Kruger 23N
    21896, # Bogota 1975 / Colombia West zone
    21897, # Bogota 1975 / Colombia Bogota zone
    21898, # Bogota 1975 / Colombia East Central zone
    21899, # Bogota 1975 / Colombia East
    22171, # POSGAR 98 / Argentina 1
    22172, # POSGAR 98 / Argentina 2
    22173, # POSGAR 98 / Argentina 3
    22174, # POSGAR 98 / Argentina 4
    22175, # POSGAR 98 / Argentina 5
    22176, # POSGAR 98 / Argentina 6
    22177, # POSGAR 98 / Argentina 7
    22181, # POSGAR 94 / Argentina 1
    22182, # POSGAR 94 / Argentina 2
    22183, # POSGAR 94 / Argentina 3
    22184, # POSGAR 94 / Argentina 4
    22185, # POSGAR 94 / Argentina 5
    22186, # POSGAR 94 / Argentina 6
    22187, # POSGAR 94 / Argentina 7
    22191, # Campo Inchauspe / Argentina 1
    22192, # Campo Inchauspe / Argentina 2
    22193, # Campo Inchauspe / Argentina 3
    22194, # Campo Inchauspe / Argentina 4
    22195, # Campo Inchauspe / Argentina 5
    22196, # Campo Inchauspe / Argentina 6
    22197, # Campo Inchauspe / Argentina 7
    25884, # ETRS89 / TM Baltic93
    27205, # NZGD49 / Mount Eden Circuit
    27206, # NZGD49 / Bay of Plenty Circuit
    27207, # NZGD49 / Poverty Bay Circuit
    27208, # NZGD49 / Hawkes Bay Circuit
    27209, # NZGD49 / Taranaki Circuit
    27210, # NZGD49 / Tuhirangi Circuit
    27211, # NZGD49 / Wanganui Circuit
    27212, # NZGD49 / Wairarapa Circuit
    27213, # NZGD49 / Wellington Circuit
    27214, # NZGD49 / Collingwood Circuit
    27215, # NZGD49 / Nelson Circuit
    27216, # NZGD49 / Karamea Circuit
    27217, # NZGD49 / Buller Circuit
    27218, # NZGD49 / Grey Circuit
    27219, # NZGD49 / Amuri Circuit
    27220, # NZGD49 / Marlborough Circuit
    27221, # NZGD49 / Hokitika Circuit
    27222, # NZGD49 / Okarito Circuit
    27223, # NZGD49 / Jacksons Bay Circuit
    27224, # NZGD49 / Mount Pleasant Circuit
    27225, # NZGD49 / Gawler Circuit
    27226, # NZGD49 / Timaru Circuit
    27227, # NZGD49 / Lindis Peak Circuit
    27228, # NZGD49 / Mount Nicholas Circuit
    27229, # NZGD49 / Mount York Circuit
    27230, # NZGD49 / Observation Point Circuit
    27231, # NZGD49 / North Taieri Circuit
    27232, # NZGD49 / Bluff Circuit
    27391, # NGO 1948 (Oslo) / NGO zone I
    27392, # NGO 1948 (Oslo) / NGO zone II
    27393, # NGO 1948 (Oslo) / NGO zone III
    27394, # NGO 1948 (Oslo) / NGO zone IV
    27395, # NGO 1948 (Oslo) / NGO zone V
    27396, # NGO 1948 (Oslo) / NGO zone VI
    27397, # NGO 1948 (Oslo) / NGO zone VII
    27398, # NGO 1948 (Oslo) / NGO zone VIII
    27492, # Datum 73 / Modified Portuguese Grid
    28402, # Pulkovo 1942 / Gauss-Kruger zone 2
    28403, # Pulkovo 1942 / Gauss-Kruger zone 3
    28404, # Pulkovo 1942 / Gauss-Kruger zone 4
    28405, # Pulkovo 1942 / Gauss-Kruger zone 5
    28406, # Pulkovo 1942 / Gauss-Kruger zone 6
    28407, # Pulkovo 1942 / Gauss-Kruger zone 7
    28408, # Pulkovo 1942 / Gauss-Kruger zone 8
    28409, # Pulkovo 1942 / Gauss-Kruger zone 9
    28410, # Pulkovo 1942 / Gauss-Kruger zone 10
    28411, # Pulkovo 1942 / Gauss-Kruger zone 11
    28412, # Pulkovo 1942 / Gauss-Kruger zone 12
    28413, # Pulkovo 1942 / Gauss-Kruger zone 13
    28414, # Pulkovo 1942 / Gauss-Kruger zone 14
    28415, # Pulkovo 1942 / Gauss-Kruger zone 15
    28416, # Pulkovo 1942 / Gauss-Kruger zone 16
    28417, # Pulkovo 1942 / Gauss-Kruger zone 17
    28418, # Pulkovo 1942 / Gauss-Kruger zone 18
    28419, # Pulkovo 1942 / Gauss-Kruger zone 19
    28420, # Pulkovo 1942 / Gauss-Kruger zone 20
    28421, # Pulkovo 1942 / Gauss-Kruger zone 21
    28422, # Pulkovo 1942 / Gauss-Kruger zone 22
    28423, # Pulkovo 1942 / Gauss-Kruger zone 23
    28424, # Pulkovo 1942 / Gauss-Kruger zone 24
    28425, # Pulkovo 1942 / Gauss-Kruger zone 25
    28426, # Pulkovo 1942 / Gauss-Kruger zone 26
    28427, # Pulkovo 1942 / Gauss-Kruger zone 27
    28428, # Pulkovo 1942 / Gauss-Kruger zone 28
    28429, # Pulkovo 1942 / Gauss-Kruger zone 29
    28430, # Pulkovo 1942 / Gauss-Kruger zone 30
    28431, # Pulkovo 1942 / Gauss-Kruger zone 31
    28432, # Pulkovo 1942 / Gauss-Kruger zone 32
    28462, # Pulkovo 1942 / Gauss-Kruger 2N
    28463, # Pulkovo 1942 / Gauss-Kruger 3N
    28464, # Pulkovo 1942 / Gauss-Kruger 4N
    28465, # Pulkovo 1942 / Gauss-Kruger 5N
    28466, # Pulkovo 1942 / Gauss-Kruger 6N
    28467, # Pulkovo 1942 / Gauss-Kruger 7N
    28468, # Pulkovo 1942 / Gauss-Kruger 8N
    28469, # Pulkovo 1942 / Gauss-Kruger 9N
    28470, # Pulkovo 1942 / Gauss-Kruger 10N
    28471, # Pulkovo 1942 / Gauss-Kruger 11N
    28472, # Pulkovo 1942 / Gauss-Kruger 12N
    28473, # Pulkovo 1942 / Gauss-Kruger 13N
    28474, # Pulkovo 1942 / Gauss-Kruger 14N
    28475, # Pulkovo 1942 / Gauss-Kruger 15N
    28476, # Pulkovo 1942 / Gauss-Kruger 16N
    28477, # Pulkovo 1942 / Gauss-Kruger 17N
    28478, # Pulkovo 1942 / Gauss-Kruger 18N
    28479, # Pulkovo 1942 / Gauss-Kruger 19N
    28480, # Pulkovo 1942 / Gauss-Kruger 20N
    28481, # Pulkovo 1942 / Gauss-Kruger 21N
    28482, # Pulkovo 1942 / Gauss-Kruger 22N
    28483, # Pulkovo 1942 / Gauss-Kruger 23N
    28484, # Pulkovo 1942 / Gauss-Kruger 24N
    28485, # Pulkovo 1942 / Gauss-Kruger 25N
    28486, # Pulkovo 1942 / Gauss-Kruger 26N
    28487, # Pulkovo 1942 / Gauss-Kruger 27N
    28488, # Pulkovo 1942 / Gauss-Kruger 28N
    28489, # Pulkovo 1942 / Gauss-Kruger 29N
    28490, # Pulkovo 1942 / Gauss-Kruger 30N
    28491, # Pulkovo 1942 / Gauss-Kruger 31N
    28492, # Pulkovo 1942 / Gauss-Kruger 32N
    29701, # Tananarive (Paris) / Laborde Grid
    29702, # Tananarive (Paris) / Laborde Grid approximation
    30161, # Tokyo / Japan Plane Rectangular CS I
    30162, # Tokyo / Japan Plane Rectangular CS II
    30163, # Tokyo / Japan Plane Rectangular CS III
    30164, # Tokyo / Japan Plane Rectangular CS IV
    30165, # Tokyo / Japan Plane Rectangular CS V
    30166, # Tokyo / Japan Plane Rectangular CS VI
    30167, # Tokyo / Japan Plane Rectangular CS VII
    30168, # Tokyo / Japan Plane Rectangular CS VIII
    30169, # Tokyo / Japan Plane Rectangular CS IX
    30170, # Tokyo / Japan Plane Rectangular CS X
    30171, # Tokyo / Japan Plane Rectangular CS XI
    30172, # Tokyo / Japan Plane Rectangular CS XII
    30173, # Tokyo / Japan Plane Rectangular CS XIII
    30174, # Tokyo / Japan Plane Rectangular CS XIV
    30175, # Tokyo / Japan Plane Rectangular CS XV
    30176, # Tokyo / Japan Plane Rectangular CS XVI
    30177, # Tokyo / Japan Plane Rectangular CS XVII
    30178, # Tokyo / Japan Plane Rectangular CS XVIII
    30179, # Tokyo / Japan Plane Rectangular CS XIX
    30800, # RT38 2.5 gon W
    31251, # MGI (Ferro) / Austria GK West Zone
    31252, # MGI (Ferro) / Austria GK Central Zone
    31253, # MGI (Ferro) / Austria GK East Zone
    31254, # MGI / Austria GK West
    31255, # MGI / Austria GK Central
    31256, # MGI / Austria GK East
    31257, # MGI / Austria GK M28
    31258, # MGI / Austria GK M31
    31259, # MGI / Austria GK M34
    31275, # MGI / Balkans zone 5
    31276, # MGI / Balkans zone 6
    31277, # MGI / Balkans zone 7
    31278, # MGI / Balkans zone 8
    31279, # MGI / Balkans zone 8
    31281, # MGI (Ferro) / Austria West Zone
    31282, # MGI (Ferro) / Austria Central Zone
    31283, # MGI (Ferro) / Austria East Zone
    31284, # MGI / Austria M28
    31285, # MGI / Austria M31
    31286, # MGI / Austria M34
    31287, # MGI / Austria Lambert
    31288, # MGI (Ferro) / M28
    31289, # MGI (Ferro) / M31
    31290, # MGI (Ferro) / M34
    31466, # DHDN / 3-degree Gauss-Kruger zone 2
    31467, # DHDN / 3-degree Gauss-Kruger zone 3
    31468, # DHDN / 3-degree Gauss-Kruger zone 4
    31469, # DHDN / 3-degree Gauss-Kruger zone 5
    31700, # Dealul Piscului 1970/ Stereo 70
    61206405, # Greek (deg)
    61216405, # GGRS87 (deg)
    61226405, # ATS77 (deg)
    61236405, # KKJ (deg)
    61246405, # RT90 (deg)
    61266405, # LKS94 (ETRS89) (deg)
    61266413, # LKS94 (ETRS89) (3D deg)
    61276405, # Tete (deg)
    61286405, # Madzansua (deg)
    61296405, # Observatario (deg)
    61306405, # Moznet (deg)
    61306413, # Moznet (3D deg)
    61316405, # Indian 1960 (deg)
    61326405, # FD58 (deg)
    61336405, # EST92 (deg)
    61346405, # PDO Survey Datum 1993 (deg)
    61356405, # Old Hawaiian (deg)
    61366405, # St. Lawrence Island (deg)
    61376405, # St. Paul Island (deg)
    61386405, # St. George Island (deg)
    61396405, # Puerto Rico (deg)
    61406405, # NAD83(CSRS) (deg)
    61406413, # NAD83(CSRS) (3D deg)
    61416405, # Israel (deg)
    61426405, # Locodjo 1965 (deg)
    61436405, # Abidjan 1987 (deg)
    61446405, # Kalianpur 1937 (deg)
    61456405, # Kalianpur 1962 (deg)
    61466405, # Kalianpur 1975 (deg)
    61476405, # Hanoi 1972 (deg)
    61486405, # Hartebeesthoek94 (deg)
    61486413, # Hartebeesthoek94 (3D deg)
    61496405, # CH1903 (deg)
    61506405, # CH1903+ (deg)
    61516405, # CHTRF95 (deg)
    61516413, # CHTRF95 (3D deg)
    61526405, # NAD83(HARN) (deg)
    61526413, # NAD83(HARN) (3D deg)
    61536405, # Rassadiran (deg)
    61546405, # ED50(ED77) (deg)
    61556405, # Dabola 1981 (deg)
    61566405, # S-JTSK (deg)
    61576405, # Mount Dillon (deg)
    61586405, # Naparima 1955 (deg)
    61596405, # ELD79 (deg)
    61606405, # Chos Malal 1914 (deg)
    61616405, # Pampa del Castillo (deg)
    61626405, # Korean 1985 (deg)
    61636405, # Yemen NGN96 (deg)
    61636413, # Yemen NGN96 (3D deg)
    61646405, # South Yemen (deg)
    61656405, # Bissau (deg)
    61666405, # Korean 1995 (deg)
    61676405, # NZGD2000 (deg)
    61676413, # NZGD2000 (3D deg)
    61686405, # Accra (deg)
    61696405, # American Samoa 1962 (deg)
    61706405, # SIRGAS (deg)
    61706413, # SIRGAS (3D deg)
    61716405, # RGF93 (deg)
    61716413, # RGF93 (3D deg)
    61736405, # IRENET95 (deg)
    61736413, # IRENET95 (3D deg)
    61746405, # Sierra Leone 1924 (deg)
    61756405, # Sierra Leone 1968 (deg)
    61766405, # Australian Antarctic (deg)
    61766413, # Australian Antarctic (3D deg)
    61786405, # Pulkovo 1942(83) (deg)
    61796405, # Pulkovo 1942(58) (deg)
    61806405, # EST97 (deg)
    61806413, # EST97 (3D deg)
    61816405, # Luxembourg 1930 (deg)
    61826405, # Azores Occidental 1939 (deg)
    61836405, # Azores Central 1948 (deg)
    61846405, # Azores Oriental 1940 (deg)
    61886405, # OSNI 1952 (deg)
    61896405, # REGVEN (deg)
    61896413, # REGVEN (3D deg)
    61906405, # POSGAR 98 (deg)
    61906413, # POSGAR 98 (3D deg)
    61916405, # Albanian 1987 (deg)
    61926405, # Douala 1948 (deg)
    61936405, # Manoca 1962 (deg)
    61946405, # Qornoq 1927 (deg)
    61956405, # Scoresbysund 1952 (deg)
    61966405, # Ammassalik 1958 (deg)
    61976405, # Garoua (deg)
    61986405, # Kousseri (deg)
    61996405, # Egypt 1930 (deg)
    62006405, # Pulkovo 1995 (deg)
    62016405, # Adindan (deg)
    62026405, # AGD66 (deg)
    62036405, # AGD84 (deg)
    62046405, # Ain el Abd (deg)
    62056405, # Afgooye (deg)
    62066405, # Agadez (deg)
    62076405, # Lisbon (deg)
    62086405, # Aratu (deg)
    62096405, # Arc 1950 (deg)
    62106405, # Arc 1960 (deg)
    62116405, # Batavia (deg)
    62126405, # Barbados 1938 (deg)
    62136405, # Beduaram (deg)
    62146405, # Beijing 1954 (deg)
    62156405, # Belge 1950 (deg)
    62166405, # Bermuda 1957 (deg)
    62186405, # Bogota 1975 (deg)
    62196405, # Bukit Rimpah (deg)
    62206405, # Camacupa (deg)
    62216405, # Campo Inchauspe (deg)
    62226405, # Cape (deg)
    62236405, # Carthage (deg)
    62246405, # Chua (deg)
    62256405, # Corrego Alegre (deg)
    62276405, # Deir ez Zor (deg)
    62296405, # Egypt 1907 (deg)
    62306405, # ED50 (deg)
    62316405, # ED87 (deg)
    62326405, # Fahud (deg)
    62336405, # Gandajika 1970 (deg)
    62366405, # Hu Tzu Shan (deg)
    62376405, # HD72 (deg)
    62386405, # ID74 (deg)
    62396405, # Indian 1954 (deg)
    62406405, # Indian 1975 (deg)
    62416405, # Jamaica 1875 (deg)
    62426405, # JAD69 (deg)
    62436405, # Kalianpur 1880 (deg)
    62446405, # Kandawala (deg)
    62456405, # Kertau (deg)
    62466405, # KOC (deg)
    62476405, # La Canoa (deg)
    62486405, # PSAD56 (deg)
    62496405, # Lake (deg)
    62506405, # Leigon (deg)
    62516405, # Liberia 1964 (deg)
    62526405, # Lome (deg)
    62536405, # Luzon 1911 (deg)
    62546405, # Hito XVIII 1963 (deg)
    62556405, # Herat North (deg)
    62566405, # Mahe 1971 (deg)
    62576405, # Makassar (deg)
    62586405, # ETRS89 (deg)
    62586413, # ETRS89 (3D deg)
    62596405, # Malongo 1987 (deg)
    62616405, # Merchich (deg)
    62626405, # Massawa (deg)
    62636405, # Minna (deg)
    62646405, # Mhast (deg)
    62656405, # Monte Mario (deg)
    62666405, # M'poraloko (deg)
    62676405, # NAD27 (deg)
    62686405, # NAD27 Michigan (deg)
    62696405, # NAD83 (deg)
    62706405, # Nahrwan 1967 (deg)
    62716405, # Naparima 1972 (deg)
    62726405, # NZGD49 (deg)
    62736405, # NGO 1948 (deg)
    62746405, # Datum 73 (deg)
    62756405, # NTF (deg)
    62766405, # NSWC 9Z-2 (deg)
    62776405, # OSGB 1936 (deg)
    62786405, # OSGB70 (deg)
    62796405, # OS(SN)80 (deg)
    62806405, # Padang (deg)
    62816405, # Palestine 1923 (deg)
    62826405, # Pointe Noire (deg)
    62836405, # GDA94 (deg)
    62836413, # GDA94 (3D deg)
    62846405, # Pulkovo 1942 (deg)
    62856405, # Qatar 1974 (deg)
    62866405, # Qatar 1948 (deg)
    62886405, # Loma Quintana (deg)
    62896405, # Amersfoort (deg)
    62926405, # Sapper Hill 1943 (deg)
    62936405, # Schwarzeck (deg)
    62956405, # Serindung (deg)
    62976405, # Tananarive (deg)
    62986405, # Timbalai 1948 (deg)
    62996405, # TM65 (deg)
    63006405, # TM75 (deg)
    63016405, # Tokyo (deg)
    63026405, # Trinidad 1903 (deg)
    63036405, # TC(1948) (deg)
    63046405, # Voirol 1875 (deg)
    63066405, # Bern 1938 (deg)
    63076405, # Nord Sahara 1959 (deg)
    63086405, # RT38 (deg)
    63096405, # Yacare (deg)
    63106405, # Yoff (deg)
    63116405, # Zanderij (deg)
    63126405, # MGI (deg)
    63136405, # Belge 1972 (deg)
    63146405, # DHDN (deg)
    63156405, # Conakry 1905 (deg)
    63166405, # Dealul Piscului 1933 (deg)
    63176405, # Dealul Piscului 1970 (deg)
    63186405, # NGN (deg)
    63196405, # KUDAMS (deg)
    63226405, # WGS 72 (deg)
    63246405, # WGS 72BE (deg)
    63266405, # WGS 84 (deg)
    63266406, # WGS 84 (degH)
    63266407, # WGS 84 (Hdeg)
    63266408, # WGS 84 (DM)
    63266409, # WGS 84 (DMH)
    63266410, # WGS 84 (HDM)
    63266411, # WGS 84 (DMS)
    63266412, # WGS 84 (HDMS)
    63266413, # WGS 84 (3D deg)
    63266414, # WGS 84 (3D degH)
    63266415, # WGS 84 (3D Hdeg)
    63266416, # WGS 84 (3D DM)
    63266417, # WGS 84 (3D DMH)
    63266418, # WGS 84 (3D HDM)
    63266419, # WGS 84 (3D DMS)
    63266420, # WGS 84 (3D HDMS)
    66006405, # Anguilla 1957 (deg)
    66016405, # Antigua 1943 (deg)
    66026405, # Dominica 1945 (deg)
    66036405, # Grenada 1953 (deg)
    66046405, # Montserrat 1958 (deg)
    66056405, # St. Kitts 1955 (deg)
    66066405, # St. Lucia 1955 (deg)
    66076405, # St. Vincent 1945 (deg)
    66086405, # NAD27(76) (deg)
    66096405, # NAD27(CGQ77) (deg)
    66106405, # Xian 1980 (deg)
    66116405, # Hong Kong 1980 (deg)
    66126405, # JGD2000 (deg)
    66126413, # JGD2000 (3D deg)
    66136405, # Segara (deg)
    66146405, # QND95 (deg)
    66156405, # Porto Santo (deg)
    66166405, # Selvagem Grande (deg)
    66186405, # SAD69 (deg)
    66196405, # SWEREF99 (deg)
    66196413, # SWEREF99 (3D deg)
    66206405, # Point 58 (deg)
    66216405, # Fort Marigot (deg)
    66226405, # Sainte Anne (deg)
    66236405, # CSG67 (deg)
    66246405, # RGFG95 (deg)
    66246413, # RGFG95 (3D deg)
    66256405, # Fort Desaix (deg)
    66266405, # Piton des Neiges (deg)
    66276405, # RGR92 (deg)
    66276413, # RGR92 (3D deg)
    66286405, # Tahiti (deg)
    66296405, # Tahaa (deg)
    66306405, # IGN72 Nuku Hiva (deg)
    66316405, # K0 1949 (deg)
    66326405, # Combani 1950 (deg)
    66336405, # IGN56 Lifou (deg)
    66346405, # IGN72 Grande Terre (deg)
    66356405, # ST87 Ouvea (deg)
    66366405, # Petrels 1972 (deg)
    66376405, # Perroud 1950 (deg)
    66386405, # Saint Pierre et Miquelon 1950 (deg)
    66396405, # MOP78 (deg)
    66406405, # RRAF 1991 (deg)
    66406413, # RRAF 1991 (3D deg)
    66416405, # IGN53 Mare (deg)
    66426405, # ST84 Ile des Pins (deg)
    66436405, # ST71 Belep (deg)
    66446405, # NEA74 Noumea (deg)
    66456405, # RGNC 1991 (deg)
    66456413, # RGNC 1991 (3D deg)
    66466405, # Grand Comoros (deg)
    66576405, # Reykjavik 1900 (deg)
    66586405, # Hjorsey 1955 (deg)
    66596405, # ISN93 (deg)
    66596413, # ISN93 (3D deg)
    66606405, # Helle 1954 (deg)
    66616405, # LKS92 (deg)
    66616413, # LKS92 (3D deg)
    66636405, # Porto Santo 1995 (deg)
    66646405, # Azores Oriental 1995 (deg)
    66656405, # Azores Central 1995 (deg)
    66666405, # Lisbon 1890 (deg)
    66676405, # IKBD-92 (deg)
    68016405, # Bern 1898 (Bern) (deg)
    68026405, # Bogota 1975 (Bogota) (deg)
    68036405, # Lisbon (Lisbon) (deg)
    68046405, # Makassar (Jakarta) (deg)
    68056405, # MGI (Ferro) (deg)
    68066405, # Monte Mario (Rome) (deg)
    68086405, # Padang (Jakarta) (deg)
    68096405, # Belge 1950 (Brussels) (deg)
    68136405, # Batavia (Jakarta) (deg)
    68146405, # RT38 (Stockholm) (deg)
    68156405, # Greek (Athens) (deg)
    68186405, # S-JTSK (Ferro) (deg)
    68206405, # Segara (Jakarta) (deg)
    69036405, # Madrid 1870 (Madrid) (deg)

])

def isAxisOrderLatLon(srsname):
    values =  srsname.split(":")
    if (values[0] == "urn"):
        try:
            if int(values[-1]) in epsg_lat_lon_order:
                return True
        except:
            return False
    return False





