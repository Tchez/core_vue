const { computed, toRefs } = Vue;

/**
 * Componente para exibir uma listagem de itens, que serão passados como propriedade no formato de lista de objetos.
 * 
 * @example
 * <list-vue items="{{ object_list }}"></list-vue>
 */
export default {        
    props: {
        items: {
            type: Array,
            required: true,
        },        
    },

    template: `
        <table>
            <thead>
                <tr>
                    <th class="table-actions" scope="col">Ações</th>
                    <th>value</th>
                    <th>Name</th>
                    <th>Index</th>
                    <th scope="col" class="table-delete"></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in items">
                    <td class="text-center">
                        <a href="#"
                        class="br-button circle primary small m-1"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        title="Visualizar">
                            <i class="fas fa-eye fa-sm"></i>
                        </a>
                        <a href="#"
                        class="br-button secondary circle small m-1"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        title="Editar">
                            <i class="fas fa-pencil-alt fa-sm"></i>
                        </a>
                    </td>
                    <td v-for="(value, name, index) in item">{{ value }}</td>
                    <td class="text-center">
                        <a href="#"
                            class="br-button circle small text-danger"
                            data-toggle="tooltip"
                            data-placement="bottom"
                            title="Excluir">
                            <i class="fas fa-trash fa-sm"></i>
                        </a>
                    </td>
                </tr>
            </tbody>
        </table>
    `
};

