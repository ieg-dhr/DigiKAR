<template>
    <div class="schema-entry" style="margin-bottom: 2em;">
        <h3 :id="name" class="name">{{ name }}
            <icon :icon="iconName" :inline="true" style="color:grey;display: inline;" />
        </h3>
        <div>
            Datatype <span class="badge">{{ type ?? "unknown" }}</span>
        </div>
        <div class="description">
            <h4>Description</h4>
            <p v-if="description">{{ description }}</p>
            <p v-else="description" class="missing">No short description provided.</p>
            <details style="margin-top: 1em;">
                <slot>
                    <p class="missing">This datatype is not yet described</p>
                </slot>
                <div v-if="examples.length" class="examples">
                    <h4>Examples</h4>
                    <div v-for="(example, index) in examples" :key="index">
                        <code>{{ example }}</code>
                    </div>
                </div>
            </details>
        </div>
    </div>
</template>

<script lang="ts">
export default {
    props: {
        name: {
            type: String,
            required: true
        },
        type: {
            type: String,
            required: true
        },
        description: {
            type: String,
            required: false
        },
        examples: {
            type: Array,
            required: false
        }
    },
    computed: {
        iconName() {
            switch (this.type) {
                case 'string': return 'octicon:typography-24';
                case 'number': return 'octicon:number-24';
                default: return 'octicon:question-24';
            }
        }
    }
}

</script>

<style scoped>
.schema-entry {
    /* margin: .5em 0; */
    transition: background-color .2s;
    font-size: 1em;
    display: flex;
    flex-direction: column;
    gap: 1em;

    .badge {
        background-color: var(--vp-code-bg);
        border-radius: 2px;
        padding: 0.25em 0.5em;
        display: inline-block;
        font-weight: bold;
        font-family: var(--vp-font-family-mono);
        margin-top: .5em;
    }

    .missing {
        color: var(--vp-c-text-3);
        font-style: italic;
    }

    .description p {
        margin: 0;
    }
}
</style>