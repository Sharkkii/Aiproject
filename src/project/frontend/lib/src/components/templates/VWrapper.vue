<template>
<div id="v-wrapper">
  <v-header></v-header>
  <v-content>
    <template v-slot:content>
      <slot name="content"></slot>
    </template>
  </v-content>
  <v-footer></v-footer>
</div>
</template>

<style scoped lang="scss">
</style>

<script>
import VHeader from "./VHeader.vue"
import VContent from "./VContent.vue"
import VFooter from "./VFooter.vue"
export default {
  name: "VWrapper",
  components: {
    VHeader,
    VContent,
    VFooter
  }
}
</script>