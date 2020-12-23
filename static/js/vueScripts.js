var comp = {
    template:'<div>{{client}}</div>',
    data: function(){
        return {
            header: 'Counter Program'
        }
    }
};

var app = new Vue({
        el: '#app',
        data: {
            client: '',

        },
        methods: {
            clientM: function(){
                this.client = 2;
            }
        },
        components:{
        'client':comp
         }
    })