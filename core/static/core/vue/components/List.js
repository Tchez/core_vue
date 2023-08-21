const { ref, onMounted, computed } = Vue;

/**
 * Componente `list-vue` para exibir uma tabela de itens.
 * 
 * @property {String} app_name - Nome da aplicação para buscar as permissões do usuário e para fazer as requisições.
 * @property {String} model_name - Nome do modelo para fazer as requisições.
 * @property {String} endpoint - Endpoint personalizado para buscar os itens. Caso não seja fornecido, um padrão será usado.
 * @property {Array} fields - Campos que serão exibidos na visualização.
 * 
 * @example
 * <list-vue 
 *     app_name="aluno" 
 *     model_name="aluno" 
 *     endpoint="/aluno/api/v1/listagem/aluno/" 
 *     :fields="['nome', 'idade', 'matricula', 'ativo']">
 * </list-vue>
 */
export default {
    props: {
        app_name: { type: String, required: true },
        model_name: { type: String, required: true },
        endpoint: { type: String, default: '' },
        fields: { type: Array, required: true },
    },


    setup(props) {
        const userPermissions = ref({});
        const items = ref([]);
        const loading = ref(false);
        const error = ref(null);


        /**
         * Faz a requisição à API para buscar as permissões do usuário logado.
         */
        const fetchPermissions = async () => {
            const url = `${window.location.origin}/usuario/api/v1/permissions/?perms=${props.app_name}.delete_${props.app_name},${props.app_name}.view_${props.app_name},${props.app_name}.change_${props.app_name}`;
            
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
         * Faz a requisição à API para buscar os itens a serem renderizados.
         */
        const fetchItems = async () => {
            const baseEndpoint = `${window.location.origin}/${props.app_name}/api/v1/listagem/${props.model_name}/`;
            const url = props.endpoint || baseEndpoint;

            try {
                loading.value = true;
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error('Erro na requisição ao tentar buscar os itens');
                }
                items.value = await response.json();                
            } catch (err) {
                console.error('Erro ao buscar itens:', err);
                error.value = err;
            } finally {
                loading.value = false;
            }
        };


        /**
         * Retorna os campos que serão renderizados na tabela.
         * Exclui os campos que não estão na lista de `fields`.
         * 
         * @returns {Array} - Campos que serão renderizados na tabela.
         */
        const fieldsToRender = computed(() => {
            if (!items.value || !items.value.results || items.value.results.length === 0) {
                return [];
            }
            return props.fields;
        });


        /**
         * Retorna os itens que serão renderizados na tabela.
         * Exclui os campos que não estão na lista de `fields`.
         *
         * @returns {Array} - Itens que serão renderizados na tabela.
         */
        const listToRender = computed(() => {
            if (!items.value || !items.value.results || items.value.results.length === 0) {
                return [];
            }
            return items.value.results.map(item => {
                const newItem = {};
                props.fields.forEach(field => {
                    newItem[field] = item[field];
                });
                return newItem;
            });
        });
        

        /**
         * Retorna a URL para a página de detalhes do item.
         * 
         * @param {Number} pk - Chave primária do item.
         * @returns {String} - URL para a página de detalhes do item.
         */
        const getDetailUrl = (pk) => {
            return `${window.location.origin}/core/${props.app_name}/${props.model_name}/${pk}/`;
        };

        /**
         * Retorna a URL para a página de edição do item.
         * 
         * @param {Number} pk - Chave primária do item a ser editado.
         * @returns {String} - URL para a página de edição do item.
         */
        const getUpdateUrl = (pk) => {
            return `${window.location.origin}/core/${props.app_name}/${props.model_name}/update/${pk}/`;
        };

        /**
         * Retorna a URL para a página de exclusão do item.
         * 
         * @param {Number} pk - Chave primária do item a ser excluído.
         * @returns {String} - URL para a página de exclusão do item.
         */
        const getDeleteUrl = (pk) => {
            return `${window.location.origin}/core/${props.app_name}/${props.model_name}/delete/${pk}/`;
        };

        /**
         * Retorna a URL para a página de restauração do item.
         * 
         * @param {Number} pk - Chave primária do item a ser restaurado.
         * @returns {String} - URL para a página de restauração do item.
         */
        const getRestoreUrl = (pk) => {
            return `${window.location.origin}/core/${props.app_name}/${props.model_name}/restore/${pk}/`;
        };

        /**
         * Verifica se um item foi excluído.
         * 
         * @param {Number} index - Índice do item na lista de resultados.
         * @returns {Boolean} - `true` se o item foi excluído, `false` caso contrário.
         */
        const isDeleted = (index) => {
            return items.value.results[index] && items.value.results[index].deleted == true;
        };

        onMounted(() => {
            fetchPermissions();
            fetchItems();
        });

        return {
            items,
            loading,
            error,
            userCanDelete: computed(() => checkPermission(`${props.app_name}.delete_aluno`)),
            userCanView: computed(() => checkPermission(`${props.app_name}.view_aluno`)),
            userCanChange: computed(() => checkPermission(`${props.app_name}.change_aluno`)),
            fieldsToRender,
            listToRender,
            getDetailUrl,
            getUpdateUrl,
            getDeleteUrl,
            getRestoreUrl,
            isDeleted,
        };
    },

    template: `
        <div>
            <div v-if="loading" class="text-center">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Carregando...</span>
                </div>
            </div>
            <div v-else-if="error" class="alert alert-danger" role="alert">
                {{ error }}
            </div>
            <div v-else>
                <table>
                    <thead>
                        <tr>
                            <th class="table-actions" scope="col">Ações</th>
                            <th v-for="field in fieldsToRender" :key="field">{{ field }}</th>
                            <th scope="col" class="table-delete"></th>
                        </tr>
                    </thead>                    
                    <tbody>                
                        <!-- Usando (renderedItem, index) no loop para pegar o item original -->
                        <tr v-for="(renderedItem, index) in listToRender" 
                            :class="{ 'deleted': isDeleted(index) }">
                            <td class="text-center">
                                <a v-if="userCanView" :href="getDetailUrl(items.results[index].id)"
                                class="br-button circle primary small m-1"
                                data-toggle="tooltip"
                                data-placement="bottom"
                                title="Visualizar">
                                    <i class="fas fa-eye fa-sm"></i>
                                </a>
                                <a v-if="userCanChange" :href="getUpdateUrl(items.results[index].id)"
                                class="br-button secondary circle small m-1"
                                data-toggle="tooltip"
                                data-placement="bottom"
                                title="Editar">
                                    <i class="fas fa-pencil-alt fa-sm"></i>
                                </a>
                            </td>
                            <td v-for="field in fieldsToRender" :key="field">
                                {{ renderedItem[field] }}
                            </td>
                            <td class="text-center">
                                <div v-if="userCanDelete">
                                    <div v-if="isDeleted(index)">
                                        <a :href="getRestoreUrl(items.results[index].id)"
                                            class="br-button circle small text-success"
                                            data-toggle="tooltip"
                                            data-placement="bottom"
                                            title="Restaurar">
                                            <i class="fas fa-trash-restore fa-sm"></i>
                                        </a>
                                    </div>
                                
                                    <div v-else>
                                        <a :href="getDeleteUrl(items.results[index].id)"
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
            </div>
        </div>
    `
};
