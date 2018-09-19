<template>
    <div id="slide-wrapper">
        <div id="slider">
            <div id="img-wrapper">
                <img class="mark" v-for="item in this.obj" v-bind:key="item.key">   
            </div>
        </div>
    </div>
</template>
<script>
import eventBus from "../event/eventBus";

let slideshow = function(bind){
    this.timer;
    this.vue = bind;
    this.obj = bind.obj;
    this.loopNum = 0;
    this.period = 4000;
    this.scrollY = 400.0;
    this.slide();
};
slideshow.prototype.slide = function(){
    let i = this.loopNum % this.obj.length;
    this.vue.changeIndex(i);
    let container = document.getElementById("img-wrapper");

    container.style.top = -(i * this.scrollY) + 'px';

    this.loopNum++;

    let bind = this;
    this.timer = setTimeout(function(){
        bind.slide();
    }, this.period);
};
export default {
    data(){
        return{
            obj:[],
            virtualImg: document.createElement("img"),
            slideObj: function(){},
        }
    },
    methods:{
        getElement(){
            return new Promise((resolve, reject)=>{
                window.setTimeout(()=>{
                    if(document.getElementsByClassName('mark')){
                        resolve();
                    }else{
                        reject();
                    }
                }, 1000);
            });
        },
        changeIndex(index){
            eventBus.$emit('changeIndex', index);
        }
    },
    mounted(){
        eventBus.$on('getCompetitions', (data)=>{
            this.obj = data;
            this.virtualImg.setAttribute("src", this.obj[0].img);

            let bind = this;
            let fetchImg = this.getElement(true).then(function(success){
                // debugger;
                let container = document.getElementById("slider");
                let competitions = document.getElementsByClassName('mark');

                for(let i = 0 ; i < competitions.length; i++){
                    competitions[i].setAttribute("src", bind.obj[i].img);
                }
                container.style.height += bind.virtualImg.height+"px";
                bind.slideObj = new slideshow(bind);
            }, function(fail){
            setTimeout(function(){fetchImg()},100);
            });   
        });
    },
    destroyed(){
        clearTimeout(this.slideObj.timer);
    }
}
</script>
<style scoped>
#slider{
    margin: 30px 0px;
    overflow: hidden;  
}
#img-wrapper{
    position: relative;
    top: 0;
    transition: 2s top;
}
#slider img{
    display: block;
    text-align: center;
    margin:0 auto;
    margin-bottom: 62px;
}
.fade-in{
    animation: fade-in 2s ease;
    animation-fill-mode: forwards;
}
.fade-out{
    animation: fade-out 2s ease;
    animation-fill-mode: forwards;
}

@keyframes fade-out{
    from{
        transform: translateY(0px);
    }
    to{
        transform: translateY(-400px);
    }
}
@keyframes fade-in{
     from{
        transform: translateY(0px);
    }
    to{
        transform: translateY(-400px);
    }
}
</style>
