const { ref, onMounted, computed } = Vue;


/**
 * Componente `list-vue` para exibir uma tabela de itens.
 * @property {Array} items - Lista de objetos a serem renderizados.
 * @property {Array} remove - Campos a serem removidos da visualização.
 * @property {String} app_name - Nome da aplicação para buscar as permissões do usuário.
 * @property {String} server_url - URL do servidor para fazer as requisições.
 * 
 * @example
 * <list-vue :items="{{ object_list|safe }} app_name="name" server_url="http://localhost:8000"></list-vue>
 */
export default {
    props: {
        items: {
            type: Array,
            required: true,
        },
        remove: {
            type: Array,
            default: () => ["deleted", "pk", "created_at", "updated_at"],
        },
        app_name: {
            type: String,
            required: true,
        },
        server_url: {
            type: String,
            required: true,
        },
    },

    setup(props) {
        const userPermissions = ref({});

        /**
         * Faz a requisição à API para buscar as permissões do usuário logado.
         */
        const fetchPermissions = async () => {
            const url = `${props.server_url}/usuario/api/v1/permissions/?perms=${props.app_name}.delete_aluno,${props.app_name}.view_aluno,${props.app_name}.change_aluno`;
            
            try {     
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error('Erro na requisição ao tentar buscar permissões do usuário logado');
                }
                userPermissions.value = await response.json();
            } catch (error) {
                console.error('Erro ao buscar permissões:', error);
            }
        };

        /**
         * Verifica se uma determinada permissão foi concedida ao usuário logado.
         * @param {String} permission - A permissão a ser verificada.
         * @returns {Boolean} - `true` se o usuário tem a permissão, `false` caso contrário.
         */
        const checkPermission = (permission) => {
            return userPermissions.value && userPermissions.value[permission] === true;
        };

        /**
         * Retorna os campos a serem renderizados na tabela.
         * Exclui os campos especificados em `remove`.
         */
        const fieldsToRender = computed(() => {
            return Object.keys(props.items[0]).filter(key => !props.remove.includes(key));
        });

        /**
         * Retorna a lista de itens a serem renderizados na tabela.
         * Exclui os campos especificados em `remove`.
         */
        const listToRender = computed(() => {
            return props.items.map(item => {
                let filteredItem = {};
                fieldsToRender.value.forEach(field => {
                    filteredItem[field] = item[field];
                });
                return filteredItem;
            });
        });

        onMounted(fetchPermissions);

        return {
            userCanDelete: computed(() => checkPermission(`${props.app_name}.delete_aluno`)),
            userCanView: computed(() => checkPermission(`${props.app_name}.view_aluno`)),
            userCanChange: computed(() => checkPermission(`${props.app_name}.change_aluno`)),
            fieldsToRender,
            listToRender
        };
    },

    template: `
        <table>
            <thead>
                <tr>
                    <th class="table-actions" scope="col">Ações</th>
                    <th v-for="field in fieldsToRender">{{field}}</th>
                    <th scope="col" class="table-delete"></th>
                </tr>
            </thead>
            <tbody>                
                <!-- Usando (renderedItem, index) no loop para pegar o item original -->
                <tr v-for="(renderedItem, index) in listToRender" 
                    :class="{ 'deleted': items[index].deleted === 'True' }">
                    <td class="text-center">
                        <a v-if="userCanView" href="#"
                        class="br-button circle primary small m-1"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        title="Visualizar">
                            <i class="fas fa-eye fa-sm"></i>
                        </a>
                        <a v-if="userCanChange" href="#"
                        class="br-button secondary circle small m-1"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        title="Editar">
                            <i class="fas fa-pencil-alt fa-sm"></i>
                        </a>
                    </td>
                    <td v-for="value in renderedItem">
                        {{ value }}
                    </td>
                    <td class="text-center">
                        <div v-if="userCanDelete">
                            <div v-if="items[index].deleted === 'True'">
                                <a href="#"
                                    class="br-button circle small text-success"
                                    data-toggle="tooltip"
                                    data-placement="bottom"
                                    title="Restaurar">
                                    <i class="fas fa-trash-restore fa-sm"></i>
                                </a>
                            </div>
                        
                            <div v-else>
                                <a href="#"
                                    class="br-button circle small text-danger"
                                    data-toggle="tooltip"
                                    data-placement="bottom"
                                    title="Excluir">
                                    <i class="fas fa-trash fa-sm"></i>
                                </a>
                            </div>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
`
};
