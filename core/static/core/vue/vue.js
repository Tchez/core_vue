import MessageVue from './components/MessageVue.js';
import TagScriptVue from './components/TagScriptVue.js';

const { createApp } = Vue;

const app = createApp({
    delimiters: ['[[', ']]'],

    data() {
        return {
            hello: 'Hello Vue!'
        }
    },
});

app.component('message-vue', MessageVue);
app.component('script-vue', TagScriptVue);
app.mount('#app');
