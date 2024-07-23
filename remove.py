#input_dir是pickle文件
with open(input_dir, 'wb')  as file:
    data = pickle.load(file)

G = data['G']

for node in G.nodes:
    if len(G.in_edges(node)) == 0 and len(G.out_edges(node)) == 0:
        G.remove_node(node)

#output_dir是目标输出文件
with open(output_dir, 'wb') as file:
    pickle.dump({"G": G,                    # 保存计算图
                 "optim_mg": data['metagraph'],      # 保存metagraph
                 "op_perf": data['op_perf'],               # 这里面包含节点的profile信息
                 "step_stats": data['step_stats'],
                 "ungrouped_mapping": data['ungrouped_mapping']}, file)  # 这里面包含了设备信息
