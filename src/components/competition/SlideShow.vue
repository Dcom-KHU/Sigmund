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
let slideshow = function(obj){
    this.obj = obj;
    this.loopNum = 0;
    this.period = 4000;
    this.scrollY = 400;
    this.slide();
};
slideshow.prototype.slide = function(){
    let i = this.loopNum % this.obj.length;
    let container = document.getElementById("img-wrapper");

    if(this.loopNum !== 0){
        if(i !== 0){
            container.style.top = parseFloat(getComputedStyle(container).top) - this.scrollY + 'px';
        }else{
            container.style.top = '0px';
        }
    }

    this.loopNum++;

    let bind = this;
    setTimeout(function(){
        bind.slide();
    }, this.period);
};
export default {
    mounted(){
        //객체 검사 후, 존재하면
        this.obj.push({name : 'name1', price : 'price1', src : require('../../assets/competition1.png')});
        this.obj.push({name : 'name2', price : 'price2', src : 'https://www.wevity.com/upload/contest/20180905195551_636f5e5c.jpg'});
        this.obj.push({name : 'name3', price : 'price3', src : 'https://www.wevity.com/upload/contest/20180827002922_63e5409e.jpg'});
        this.obj.push({name : 'name4', price : 'price4', src : 'https://www.wevity.com/upload/contest/20180802080737_2143b5a0.jpg'});

        this.virtualImg.setAttribute("src", this.obj[0].src);
        
        let bind = this;
        let fetchImg = this.getElement(true).then(function(success){
            let container = document.getElementById("slider");
            let competitions = document.getElementsByClassName('mark');

            for(let i = 0 ; i < competitions.length; i++){
                competitions[i].setAttribute("src", bind.obj[i].src);
                console.log(competitions[i])
            }
            container.style.height += bind.virtualImg.height+"px";
            new slideshow(bind.obj);

        }, function(fail){
            setTimeout(function(){fetchImg()},100);
        });
    },
    data(){
        return{
            obj:[],
            virtualImg: document.createElement("img"),
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
        }
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
