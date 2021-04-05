<template>

    <div class="card"
         style="border-color: coral;background-color:rgba(255,255,255,0.5);">
        <div class="card-header">
            <div class="ribbon card-header-title subtitle is-capitalized is-5"
                 style="position:absolute;z-index: 100;">
                <p class="ribbon">
                    <span class="text"><strong class="bold">
                {{name}}</strong> {{description}}</span>
                </p>
            </div>
        </div>
        <div class="card-content has-text-centered" style="margin-top:-24px">
            <div class=" card-image has-text-centered">
                <figure class="inline-block">
                    <img :src="require('@/assets/img/products/' + img)"/>
                </figure>
            </div>
        </div>
        <div class="card-footer"
             style="position: absolute;bottom: 0;width: 100%;background-color:rgba(128,128,128,0.8)">
            <div v-if="description !== ''" class="card-footer-item" style="color: white;padding:0">
                {{description}}
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
                type: Number,
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
        position: relative;
        display: inline-block;
        text-align: center;
    }

    .text {
        display: inline-block;
        padding: 0.5em 1em;
        min-width: 20em;
        line-height: 1.2em;
        background: #FFD72A;
        position: relative;
    }

    .ribbon:after, .ribbon:before,
    .text:before, .text:after,
    .bold:before {
        content: '';
        position: absolute;
        border-style: solid;
    }

    .ribbon:before {
        top: 0.3em;
        left: 0.2em;
        width: 100%;
        height: 100%;
        border: none;
        background: #EBECED;
        z-index: -2;
    }

    .text:before {
        bottom: 100%;
        left: 0;
        border-width: .5em .7em 0 0;
        border-color: transparent #FC9544 transparent transparent;
    }

    .text:after {
        top: 100%;
        right: 0;
        border-width: .5em 2em 0 0;
        border-color: #FC9544 transparent transparent transparent;
    }

    .ribbon:after, .bold:before {
        top: 0.5em;
        right: -2em;
        border-width: 1.1em 1em 1.1em 3em;
        border-color: #FECC30 transparent #FECC30 #FECC30;
        z-index: -1;
    }

    .bold:before {
        border-color: #EBECED transparent #EBECED #EBECED;
        top: 0.7em;
        right: -2.3em;
    }

</style>
