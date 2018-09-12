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
            isScroll : false,
        }
    },
    methods:{
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
                console.log("up");
                if(this.page.currentPage > this.page.getFirstPage()){
                    this.page.currentPage -= 1;
                    this.smoothScroll(this.page.currentPage);
                }
            }
	        else{
                console.log("down");
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
</style>