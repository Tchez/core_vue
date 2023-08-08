const { createApp, computed, toRefs } = Vue;

const MyAlert = {
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
    `
};

const app = createApp({
    delimiters: ['[[', ']]'],

    data() {
        return {
            message: 'Hello Vue!'
        }
    },
});

app.component('my-alert', MyAlert);
app.mount('#app');
