<template>
    <Layout>
        <template v-if="$frontmatter.authors && $frontmatter.authors.length > 0" #doc-footer-before>
            <!-- <template #doc-footer-before> -->
            <div class="author-info">
                Authors: <span v-for="(author, index) in $frontmatter.authors" :key="index">
                    {{ author }}<template v-if="index < $frontmatter.authors.length - 1">, </template>
                </span>
            </div>
        </template>
    </Layout>
</template>

<script setup lang="ts">
import DefaultTheme from 'vitepress/theme'
import { useData } from 'vitepress'
import { watchEffect } from 'vue'
import { inBrowser } from './utils'

const { Layout } = DefaultTheme
const { lang } = useData()

watchEffect(() => {
    if (inBrowser) {
        document.cookie = `nf_lang=${lang.value}; expires=Mon, 1 Jan 2030 00:00:00 UTC; path=/`
    }
})
</script>

<style scoped>
.author-info {
    font-size: 14px;
    font-weight: 500;
    color: var(--vp-c-text-2)
}
</style>