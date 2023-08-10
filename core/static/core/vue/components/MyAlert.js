const { computed, toRefs } = Vue;

/**
 * Componente de alerta para exibir mensagens de sucesso, erro, alerta e informação.
 * 
 * @example
 * <my-alert></my-alert>
 * <my-alert type="success" message="Mensagem de sucesso!"></my-alert>
 * <my-alert type="danger" message="Mensagem de erro!"></my-alert>
 * <my-alert type="warning" message="Mensagem de alerta!"></my-alert>
 * <my-alert type="info" message="Mensagem de informação!"></my-alert>
 */
export default {        
    props: {
        type: {
            default: 'success',
            type: String
        },
        message: {
            default: 'Mensagem padrão! Lembre-se de alterar usando a propriedade message',
            type: String
        }
    },

    setup(props) {
        const alertClass = computed(() => {
            return ["br-message rounder-md", props.type ? `${props.type}` : ""].filter(Boolean).join(' ');
        });

        return {
            ...toRefs(props),
            alertClass
        };
    },

    template: `
        <div>   
            <div :class="alertClass" role="alert">
                <div class="content">
                    <span class="message-title">{{ message }}</span><span class="message-body"></span>
                </div>
                <div class="close">
                    <button class="br-button circle small" type="button" aria-label="Fechar">
                        <i class="fas fa-times" aria-hidden="true"></i>
                    </button>
                </div>
            </div>
        </div>
    `
};

