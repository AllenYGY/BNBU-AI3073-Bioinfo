def ExonChaining(G, n):
    # G 是一个包含区间元组的列表，每个元组为 (左端点, 右端点, 权重)
    # n 是区间数量
    # 初始化动态规划数组和选择的区间记录
    s = [0] * (2 * n + 1)
    selected_intervals = [[] for _ in range(2 * n + 1)]  # 用于记录每个端点的选择区间
    
    # 创建所有端点的列表，并为其进行排序
    endpoints = sorted(set([v for interval in G for v in interval[:2]]))  # 获取去重后的所有端点
    endpoint_index = {v: i+1 for i, v in enumerate(endpoints)}  # 为每个端点分配索引值
    
    # 初始化区间表，记录每个区间的左、右端点索引和权重
    intervals = [(endpoint_index[l], endpoint_index[r], w) for l, r, w in G]
    for i in range(1, len(endpoints) + 1):
        right_intervals = [interval for interval in intervals if interval[1] == i]
        
        if right_intervals:
            for l, r, w in right_intervals:
                s[i] = max(s[i-1], s[l] + w)
                # 如果选择了当前区间，更新选择的区间记录
                if s[i] == s[l] + w:
                    selected_intervals[i] = selected_intervals[l] + [(endpoints[l-1], endpoints[r-1], w)]
        else:
            # 如果没有选择任何区间，则继承前一个端点的选择和权重
            s[i] = s[i - 1]
            selected_intervals[i] = selected_intervals[i - 1]
    
    # 返回最优解的最大权重和选择的区间
    return s, selected_intervals[len(endpoints)]

# 定义区间 (左端点, 右端点, 权重)
G = [
    (1, 5, 5),   
    (2, 3, 3),   
    (4, 8, 6),   
    (6, 12, 10),  
    (7, 17, 12),   
    (9, 10, 1),  
    (11, 15, 7),  
    (13, 14, 0),  
    (16, 18, 4)  
]
G2=[
    (1, 5, 4),   
    (2, 3, 5),   
    (4, 8, 11),   
    (6, 12, 8),  
    (7, 17, 9),   
    (9, 10, 0),  
    (11, 15, 6),  
    (13, 14, 3),  
    (16, 18, 2)  
]
s, selected = ExonChaining(G2, len(G2))
print("最大不重叠区间的总权重为:", s)
print("选择的区间为:", selected)