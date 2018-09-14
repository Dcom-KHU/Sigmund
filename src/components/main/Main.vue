<template>
    <div id="view-wrapper">
        <Navigation></Navigation>
        <div>
            <div class="content">
                <div id="intro">
                    <div>Hi,</div>
                    <div>We're D.com,</div>
                    <div class="typewrite" data-period="1000" data-type='[ "web developer.", "data analysist.", "AI developer.", "game programmer." ]'></div>
                </div>
            </div>
            <div class="content"></div>
        </div>
        <Footer></Footer>
    </div>
</template>
<script>
import Navigation from '../fixed/Navigation'
import Footer from '../fixed/Footer'

let TxtType = function(el, rotate, period){
    this.rotate = rotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.txt = '';
    this.tick();
    this.isDeleteing = false;
}

TxtType.prototype.tick = function(){
    let i = this.loopNum % this.rotate.length;
    let fullTxt = this.rotate[i];

    if(this.isDeleteing){
        this.txt = fullTxt.substring(0, this.txt.length-1);
    }else{
        this.txt = fullTxt.substring(0, this.txt.length+1);
    }

    this.el.innerHTML = '<span>'+this.txt+'</span>';

    let bind = this;
    let delta = 200 - Math.random() * 100;

    if(this.isDeleteing){ delta /= 2; }

    if(!this.isDeleteing && this.txt === fullTxt){
        delta = this.period;
        this.isDeleteing = true;
    }else if(this.isDeleteing && this.txt === ''){
        this.isDeleteing = false;
        this.loopNum++;
        delta = 500;
    }

    setTimeout(function(){
        bind.tick();
    }, delta);
}

export default {
    components: {
        Navigation, 
        Footer, 
    },
    data(){
        return{
            page: {
                height: 0,
                currentPage: 0,
                pages: [],
                pageCount: 2,
                getFirstPage(){
                    return this.pages[0];
                },
                getLastPage(){
                    return this.pages[this.pages.length-1];
                },
                createPage(){
                    for(let i = 0; i < this.pageCount; i++){
                        this.pages.push(i);
                    }
                    this.currentPage = this.getFirstPage();
                    this.height = window.innerHeight;
                }
            },
            scrollPos : 0,
        }
    },
    methods:{
        //화면 스크롤에 관한 method
        smoothScroll(index){
            window.scrollTo({
                top: index * this.page.height,
                behavior: "smooth"
            })
            document.body.style.height = "100%";
            document.body.style.overflow = "hidden";

            setTimeout(()=>{document.body.removeAttribute("style");}, 550);
        },
        handleScroll(ev){
            if ((document.body.getBoundingClientRect()).top > this.scrollPos){
                if(this.page.currentPage > this.page.getFirstPage()){
                    this.page.currentPage -= 1;
                    this.smoothScroll(this.page.currentPage);
                }
            }
	        else{
                if(this.page.currentPage < this.page.getLastPage()){
                    this.page.currentPage += 1;
                    this.smoothScroll(this.page.currentPage);
                }
            }
	        this.scrollPos = (document.body.getBoundingClientRect()).top;
        }
    },
    created(){
        this.page.createPage();
        window.addEventListener('scroll', this.handleScroll);
    },
    mounted(){
        let elements = document.getElementsByClassName('typewrite');
        console.log(elements.length);
        for(var i = 0; i < elements.length; i++){
            let rotate = elements[i].getAttribute('data-type');
            let period = elements[i].getAttribute('data-period');
            if(rotate){
                new TxtType(elements[i], JSON.parse(rotate), period);
            }
        }
    },
    destroyed(){
        window.removeEventListener('scroll', this.handleScroll);
    } 
}
</script>
<style scoped>
.content{
    height: 100vh;
}
.content:nth-of-type(1){
    background-color: #252627;
}
.content:nth-of-type(2){
    background-color: #ffffff;
}
#intro{
    position: absolute;
    text-align: start;
    font-weight: 500;
    font-size: 50px;
    color: #ffffff;
    top: 100px;
    left: 100px;
    letter-spacing: -2px;
    line-height: 1.0;
}
</style>