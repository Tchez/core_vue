import Message from './components/Message.js';
import TagScript from './components/TagScript.js';
import List from './components/List.js';

const { createApp } = Vue;

const app = createApp({
    delimiters: ['[[', ']]'],

    data() {
        return {
            hello: 'Hello Vue!'
        }
    },
});

app.component('message-vue', Message);
app.component('script-vue', TagScript);
app.component('list-vue', List);
app.mount('#app');
