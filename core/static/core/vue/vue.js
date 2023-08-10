import MyAlert from './components/MyAlert.js';
import ScriptImport from './components/ScriptImport.js';

const { createApp } = Vue;

const app = createApp({
    delimiters: ['[[', ']]'],

    data() {
        return {
            hello: 'Hello Vue!'
        }
    },
});

app.component('my-alert', MyAlert);
app.component('script-import', ScriptImport);
app.mount('#app');
