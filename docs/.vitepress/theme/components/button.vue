<template>
    <button class="button">
        <a :href="link">
            {{ label }}
        </a>
    </button>
</template>

<script lang="ts">
export default {
    props: {
        label: {
            type: String,
            required: true
        },
        link: {
            type: String,
            required: true
        }
    }
}
</script>

<style scoped>
.button {
    padding: .5em .75em;
    border-radius: .25em;
    background-color: rgb(240,240,240);
    transition: background-color .2s;
    font-size: 1em;
    &:hover {
        background-color: rgb(220,220,220);
    }

    a {
        text-decoration: none;
        color: black;
    }
}
</style>