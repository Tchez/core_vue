/**
 * Componente para importar scripts externos dentro de templates.
 *  
 * 
 * @example
 * <script-import src="https://google.com/jsapi"></script-import>
 * <script-import type="text/javascript">alert('Hello World!');</script-import>
 */
export default {
    props: {
        src: {
            type: String,
            default: ''
        },
        type: {
            type: String,
            default: ''
        }
    },
    
    mounted() {
        const script = document.createElement('script');
        
        if (this.type) {
            script.type = this.type;
        }
        
        if (this.src) {
            script.src = this.src;
        } else if (this.$slots.default) {
            // usa o conteúdo do slot como conteúdo do script
            const slotContent = this.$slots.default().map(vnode => vnode.children).join('');
            script.textContent = slotContent;
        }

        document.head.appendChild(script);        
    },

    template: '<div v-if="false"><slot></slot></div>'
}