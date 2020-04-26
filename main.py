import random
import gene as gcls
from decimal import Decimal
import params

def create_genes():
    genes = [random.randint(0,1) for i in range(params.GENE_LENGTH)]
    return gcls.gene_status(genes, 0)

def select_elites(gcls_list):
    sorted_list = sorted(gcls_list, key=lambda x: x.evl, reverse=True)
    elite_list = [sorted_list.pop(0) for _ in range(params.SELECT_GENE)]
    return elite_list

def swap_genes(gcls1, gcls2):
    id1 = random.randint(0, params.GENE_LENGTH)
    id2 = random.randint(id1, params.GENE_LENGTH)
    genes1, genes2 = gcls1.get_genes(), gcls2.get_genes()
    swapped_gene1 = genes1[:id1]+genes2[id1:id2]+genes1[id2:]
    swapped_gene2 = genes2[:id1]+genes1[id1:id2]+genes2[id2:]
    return [gcls.gene_status(swapped_gene1, 0), gcls.gene_status(swapped_gene2, 0)]

def change_generation(gcls_list, elite_list, children_list):
    next_generation_list = sorted(gcls_list, key=lambda x: x.evl, reverse=False)
    for _ in range(len(elite_list)+len(children_list)):
        next_generation_list.pop(0)
    next_generation_list.extend(elite_list)
    next_generation_list.extend(children_list)
    return next_generation_list

def mutate_genes(gcls_list):
    mutated_gcls_list = []
    for i in gcls_list:
        if params.INDIVISUAL_MUTATION > (random.randint(0,100)/Decimal(100)):
            mutated_genes = []
            for j in i.get_genes():
                if params.GENE_MUTATION > (random.randint(0,100)/Decimal(100)):
                    mutated_genes.append(random.randint(0, 1))
                else:
                    mutated_genes.append(j)
            i.set_genes(mutated_genes)
        mutated_gcls_list.append(i)
    return mutated_gcls_list

if __name__ == "__main__":
    current_generation = [create_genes() for i in range(params.MAX_GENE_GROUP)]
    for g in range(1, params.MAX_GENERATION+1):
        for e in range(params.MAX_GENE_GROUP):
            current_generation[e].set_evl()
        elite_list = select_elites(current_generation)
        swapped_list = []
        for s in range(params.SELECT_GENE):
            swapped_list.extend(swap_genes(elite_list[s-1],elite_list[s]))
        next_generation = change_generation(current_generation, elite_list, swapped_list)
        next_generation = mutate_genes(next_generation)

        evl_list = [i.get_evl() for i in current_generation]
        min_, max_, avr_ = min(evl_list), max(evl_list), sum(evl_list) / Decimal(len(evl_list))

        print("-----第{}世代の結果-----".format(g))
        print("  Min:{}".format(min_))
        print("  Max:{}".format(max_))
        print("  Avg:{}".format(avr_))
        if(min_ == max_):
            print("最強集団完成！")
            break
        current_generation = next_generation
    print("最も優れた個体は{}".format(elite_list[0].get_genes()))

