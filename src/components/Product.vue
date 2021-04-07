<template>

    <div class="card"
         style="border-color: coral;background-color:rgba(255,255,255,0.5);">
        <div class="card-header">
            <div class="subtitle is-capitalized is-5"
                 style="position:absolute;z-index: 100;">

                <div class=" subtitle is-bold is-2 box" style="background-color:rgba(255,115,0,0.7);
                padding-top: 0;margin-left:5px;margin-top: 5px; -webkit-transform: rotate(5deg);
            ">
                    {{price}}€
                </div>

            </div>
        </div>
        <div class=" has-text-centered" style="">
            <div class=" card-image has-text-centered">
                <figure class="inline-block">
                    <img :src="require('@/assets/img/products/' + img)"/>
                </figure>
            </div>
        </div>
        <div class="card-footer"
             style="position: absolute;bottom: 0;width: 100%;background-color:rgba(128,128,128,0.8)">
            <div class="card-footer-item" style="color: white;padding:0">
                {{name}}
            </div>

        </div>

    </div>
</template>

<script>
    export default {
        name: 'Product',
        props: {
            name: {
                type: String,
                required: true
            },
            description: {
                type: String,
                default: ''
            },
            img: {
                type: String,
                required: true
            },
            price: {
                type: String,
                required: true
            },
            old_price: {
                type: Number,
                default: 0
            },
            is_highlight: {
                type: Boolean,
                default: false
            }
        }
    };

</script>

<style scoped>
    .subtitle:not(:last-child) {
        margin-bottom: 0;
    }

    img {
        max-width: 100%;
        height: 33vh;
        width: auto;
    }

    .ribbon {
        margin-bottom: 30px;
        background-size: cover;
        text-transform: uppercase;
        color: #000000;
    }

    .ribbon:nth-child(even) {
        margin-right: 4%;
    }

    @media (max-width: 500px) {
        .ribbon {
            width: 100%;
        }

        .ribbon:nth-child(even) {
            margin-right: 0;
        }
    }

    .ribbon1 {
        position: absolute;
        top: -6.1px;
        right: 10px;
    }

    .ribbon1:after {
        position: absolute;
        content: "";
        width: 0;
        height: 0;
        border-left: 53px solid transparent;
        border-right: 53px solid transparent;
        border-top: 10px solid #F8463F;
    }

    .ribbon1 span {
        position: relative;
        display: block;
        text-align: center;
        background: #F8463F;
        font-size: 14px;
        line-height: 1;
        padding: 12px 8px 10px;
        border-top-right-radius: 8px;
        width: 90px;
    }

    .ribbon1 span:before, .ribbon1 span:after {
        position: absolute;
        content: "";
    }

    .ribbon1 span:before {
        height: 6px;
        width: 6px;
        left: -6px;
        top: 0;
        background: #F8463F;
    }

    .ribbon1 span:after {
        height: 6px;
        width: 8px;
        left: -8px;
        top: 0;
        border-radius: 8px 8px 0 0;
        background: #C02031;
    }

    .ribbon2 {
        width: 60px;
        padding: 10px 0;
        position: absolute;
        top: -6px;
        left: 25px;
        text-align: center;
        border-top-left-radius: 3px;
        background: #F47530;
    }

    .ribbon2:before {
        height: 0;
        width: 0;
        right: -5.5px;
        top: 0.1px;
        border-bottom: 6px solid #8D5A20;
        border-right: 6px solid transparent;
    }

    .ribbon2:before, .ribbon2:after {
        content: "";
        position: absolute;
    }

    .ribbon2:after {
        height: 0;
        width: 0;
        bottom: -29.5px;
        left: 0;
        border-left: 30px solid #F47530;
        border-right: 30px solid #F47530;
        border-bottom: 30px solid transparent;
    }

    .ribbon3 {
        width: 150px;
        height: 50px;
        line-height: 50px;
        padding-left: 15px;
        position: absolute;
        left: -8px;
        top: 20px;
        background: #59324C;
    }

    .ribbon3:before, .ribbon3:after {
        content: "";
        position: absolute;
    }

    .ribbon3:before {
        height: 0;
        width: 0;
        top: -8.5px;
        left: 0.1px;
        border-bottom: 9px solid black;
        border-left: 9px solid transparent;
    }

    .ribbon3:after {
        height: 0;
        width: 0;
        right: -14.5px;
        border-top: 25px solid transparent;
        border-bottom: 25px solid transparent;
        border-left: 15px solid #59324C;
    }

    .ribbon4 {
        position: absolute;
        top: 15px;
        padding: 8px 10px;
        background: rgba(0, 179, 237, 0.5);
        box-shadow: -1px 2px 3px rgba(0, 0, 0, .3);
    }

    .ribbon4:before, .ribbon4:after {
        content: "";
        position: absolute;
    }

    .ribbon4:before {
        width: 7px;
        height: 100%;
        top: 0;
        left: -6.5px;
        padding: 0 0 7px;
        background: inherit;
        border-radius: 5px 0 0 5px;
    }

    .ribbon4:after {
        width: 5px;
        height: 5px;
        bottom: -5px;
        left: -4.5px;
        background: lightblue;
        border-radius: 5px 0 0 5px;
    }

    .ribbon5 {
        display: block;
        height: 50px;
        line-height: 50px;
        text-align: center;
        margin-left: -10px;
        margin-right: -10px;
        background: #EDBA19;
        position: relative;
        top: 20px;
    }

    .ribbon5:before, .ribbon5:after {
        content: "";
        position: absolute;
    }

    .ribbon5:before {
        height: 0;
        width: 0;
        bottom: -10px;
        left: 0;
        border-top: 10px solid #cd8d11;
        border-left: 10px solid transparent;
    }

    .ribbon5:after {
        height: 0;
        width: 0;
        right: 0;
        bottom: -10px;
        border-top: 10px solid #cd8d11;
        border-right: 10px solid transparent;
    }

    .wrap {
        width: 100%;
        height: 188px;
        position: absolute;
        top: -8px;
        left: 8px;
        overflow: hidden;
    }

    .wrap:before, .wrap:after {
        content: "";
        position: absolute;
    }

    .wrap:before {
        width: 40px;
        height: 8px;
        right: 100px;
        background: #4D6530;
        border-radius: 8px 8px 0px 0px;
    }

    .wrap:after {
        width: 8px;
        height: 40px;
        right: 0px;
        top: 100px;
        background: #4D6530;
        border-radius: 0px 8px 8px 0px;
    }

    .ribbon6 {
        width: 200px;
        height: 40px;
        line-height: 40px;
        position: absolute;
        top: 30px;
        right: -50px;
        z-index: 2;
        overflow: hidden;
        -webkit-transform: rotate(45deg);
        transform: rotate(45deg);
        border: 1px dashed;
        box-shadow: 0 0 0 3px #57DD43, 0px 21px 5px -18px rgba(0, 0, 0, 0.6);
        background: #57DD43;
        text-align: center;
    }
</style>
