import argparse
import pandas as pd
from KG_utils import *

def parse_input():
    parser = argparse.ArgumentParser(description="Filter node types")
    
    parser.add_argument('node_path', type=str, help='Path to the CSV file containing the nodes')
    parser.add_argument('edge_path', type=str, help='Path to the CSV file containing the edges')
    
    parser.add_argument('-on', '--output_nodes', type=str, help='Path to save the output nodes CSV file (optional)')
    parser.add_argument('-oe', '--output_edges', type=str, help='Path to save the output edges CSV file (optional)')
    
    args = parser.parse_args()
    node_path = args.node_path
    edge_path = args.edge_path
    output_nodes = args.output_nodes
    output_edges = args.output_edges
    
    return node_path, edge_path, output_nodes, output_edges
if __name__ == '__main__':
    node_path, edge_path, output_nodes, output_edges = parse_input()
    nodes = pd.read_csv(node_path, low_memory=False)
    edges = pd.read_csv(edge_path,  low_memory=False)
    node_types = nodes['type'].unique()
    node_types_to_keep = ['Gene','Genomic feature','Protein','Disease','GO', 'Phenotype']
    node_types_to_remove = [t for t in node_types if t not in node_types_to_keep]
    
    nodes_kept, edges_kept = nodes, edges
    for type in node_types_to_remove:
        print("Removing nodes of type", type)
        nodes_kept, edges_kept = remove_node_type(nodes_kept, edges_kept, type)
        
    if output_nodes:
        nodes_kept.to_csv(output_nodes, index=False)
        print(f"Output nodes saved to {output_nodes}")
        
    if output_edges:        
        edges_kept.to_csv(output_edges, index=False)
        print(f"Output edges saved to {output_edges}")
        
    
        
    