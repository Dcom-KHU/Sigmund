<template>
    <div id="view-wrapper">
        <Navigation></Navigation>
        <div>
            <div class="content">11</div>
            <div class="content">22</div>
        </div>
        <Footer></Footer>
    </div>
</template>
<script>
import Navigation from './Navigation'
import Footer from './Footer'
// import FullPage from 'vue-fullpage.js'

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
        smoothScroll(index){
            window.scrollTo({
                top: index * this.page.height,
                behavior: "smooth"
            })
            this.preventScroll();
        },
        preventScroll(){
            addEventListener("scroll", function(e){
                e.preventDefault();
                e.returnValue = false;
            });

            setTimeout(function(){
                removeEventListener("scroll", function(e){
                    e.preventDefault();
                    e.returnValue = false;
                });
            }, 3000);
        },
        handleScroll(ev){
            // console.log(this.scrollPos);
            // detects new state and compares it with the new one
            if ((document.body.getBoundingClientRect()).top > this.scrollPos){
                //up
                if(this.page.currentPage > this.page.getFirstPage()){
                    this.page.currentPage -= 1;
                    this.smoothScroll(this.page.currentPage);
                }
            }
	        else{
                //down
                if(this.page.currentPage < this.page.getLastPage()){
                    this.page.currentPage += 1;
                    this.smoothScroll(this.page.currentPage);
                }
            }
	        // saves the new position for iteration.
	        this.scrollPos = (document.body.getBoundingClientRect()).top;
        }
    },
    created(){
        this.page.createPage();
        window.addEventListener('scroll', this.handleScroll);
    },
    destroyed(){
        window.removeEventListener('scroll', this.handleScroll);
    } 
}
</script>
<style scoped>
.content{
    height: 740px;
}
.content:nth-of-type(1){
    background-color: #252627;
}
.content:nth-of-type(2){
    background-color: #ffffff;
}
.stop-scrolling{
    height: 100%;
    overflow: hidden;
}
</style>