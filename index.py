gramatica = {
    'S': ['aAd', 'A'],
    'A': ['Bc', 'λ'],
    'B': ['Ac', 'a'],
}

def inicio(gramatica):
    terminals = set()
    renamed_terminals = {}
    next_number = 1

    for productions in gramatica.values():
        for production in productions:
            terminals.update([symbol for symbol in production if symbol.isupper()])

    for nt in terminals:
        if nt.startswith('A') and nt[1:].isdigit():
            renamed_terminals[nt] = nt
        else:
            renamed_terminals[nt] = f'A{next_number}'
            next_number += 1

    updated_grammar = {}

    # Atualiza as produções com os novos nomes
    for nt, productions in gramatica.items():
        updated_productions = []

        for production in productions:
            updated_production = production
            for old_nonterminal, new_nonterminal in renamed_terminals.items():
                updated_production = updated_production.replace(old_nonterminal, new_nonterminal)

            updated_productions.append(updated_production)

        updated_grammar[renamed_terminals.get(nt, nt)] = updated_productions

    return updated_grammar
def print_grammar(gramatica):
    for nt, productions in gramatica.items():
        print(f"{nt} -> {' | '.join(productions)}")

def remove(gramatica):
    for nt, productions in gramatica.items():
        gramatica[nt] = [production for production in productions if production != 'λ']

remove(gramatica)
updated_grammar = inicio(gramatica)
print_grammar(updated_grammar)
