<template>
    <div id="competition-wrapper">
        <Navigation></Navigation>
            <div id="competition-view">
                <span class="competition-items">
                    <div id="state">
                        <div>
                            <i class="fas fa-ellipsis-h"></i>
                            <div>D.com2.4GHz</div>
                            <i class="fas fa-wifi"></i>
                            <div>09:00PM</div>
                        </div>
                        <div>
                            <i class="fas fa-battery-quarter"></i>
                        </div>
                    </div>
                    <div id="top">
                        <i class="fas fa-camera-retro"></i>
                        <img src="../../assets/dcomstagram.png" alt="">
                        <i class="fab fa-telegram-plane"></i>
                    </div>
                    <div id="account">
                        <div>
                            <div></div>
                            <div>dcom_official</div>
                        </div>
                        <div>
                            <i class="fas fa-ellipsis-h"></i>
                        </div>
                    </div>
                    <slide-wrapper v-on:changeIndex="changeCompetitionIndex">
                    </slide-wrapper>
                    <div id="user-function">
                        <div>
                            <i class="far fa-heart"></i>
                            <i class="far fa-comment"></i>
                            <i class="far fa-paper-plane"></i>
                        </div>
                        <div>
                            <i class="far fa-bookmark"></i>
                        </div>
                    </div>
                    <div id="detail">
                        <div id="like">
                            like 258
                        </div>
                        <div>
                            <span>dcom_offical</span>
                            <change-detail v-bind:competitionIndex="competitionIndex">
                            </change-detail>
                        </div>
                    </div>
                </span>
            </div>
        <Footer></Footer>
    </div>
</template>
<script>
import eventBus from '../event/eventBus'
import Navigation from '../fixed/Navigation'
import Footer from '../fixed/Footer'
import slideWrapper from './SlideShow'
import changeDetail from './changeDetail'

export default {
    components: {
        Navigation, 
        Footer, 
        slideWrapper,
        changeDetail,
    },
    data(){
        return{
            competitions: [],
            competitionIndex: 0,
            likeElement: {},
        }
    },
    methods:{
        getCompetitions(){
            let bind = this;
            const url = 'http://13.125.196.191:8888/';
            this.$http.get(`${url}`).then(
                function(success){
                    bind.competitions = success.data;
                    eventBus.$emit('getCompetitions', bind.competitions);
                }
            ).catch(function(error){
                console.log(error);
            });
        },
        changeCompetitionIndex(index){
            this.competitionIndex = index;
        },
        randomLike(){

        }
    },
    created(){
        eventBus.$on('changeIndex', (index)=>{this.changeCompetitionIndex(index)});
        this.getCompetitions();
    },
    mounted(){
        this.likeElement = document.getElementById("like");
    },
    watch:{
        competitionIndex(){
            this.likeElement.innerText = function(max, min){
                return `like ${parseInt(Math.random() * (max - min) + min)}`;
            }(1000, 1);
        }
    }
}
</script>
<style scoped>
#competition-wrapper{
    height: 100vh;
}
#competition-view{
    padding-left: 100px;
    padding-right: 50px;
    height: inherit;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    border: 1px solid black;
}
.competition-items{
    /* height: 680px; */
    height: 730px;
    width: 414px;
    border-top: 1px solid black;
    border-bottom: 1px solid black;
    overflow: hidden;
}
#state{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}
#state > div:nth-of-type(1){
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    font-size: 10px;
    font-weight: 700;
    width: 50%;
}
#state > div:nth-of-type(1) > i:nth-of-type(1){
    font-size: 20px;
}
#top{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: inherit;
    border-bottom: 0.1px solid gray;
    font-size: 25px;
}
#top > i:nth-of-type(1){
    position: relative;
    left: 10px;
}
#top > i:nth-of-type(2){
    position: relative;
    right: 10px;
}
#top > img{
    width: 120px;
    height: 32px;
}
#account{
    padding: 10px 0px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid gray;
}
#account > div:nth-of-type(1){
    display: flex;
    align-items: center;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: -0.5px;
}
#account > div:nth-of-type(1) > div:nth-of-type(1){
    margin: 0px 8px;
    height: 40px;
    width: 40px;
    background-color: #bbb;
    border-radius: 50%;
}
#account > div:nth-of-type(2){
    padding-right: 12px;
}
#img{
    margin: 30px 0px;
}
#user-function{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid black;
    font-size: 24px;
    padding: 5px 8px;
}
#user-function > div:nth-of-type(1){
    width: 100px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}
#detail{
    display: flex;
    flex-direction: column;
    text-align: start;
}
#detail > div:nth-of-type(1), #detail > div:nth-of-type(2) > span:nth-of-type(1){
    font-size: 14px;
    font-weight: 700;
}
</style>
