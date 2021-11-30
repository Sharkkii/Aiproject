<template>
<div id="v-index">
  <v-wrapper>
    <template v-slot:content>
      <v-dashboard></v-dashboard>
    </template>
  </v-wrapper>
</div>
</template>

<script>
import VWrapper from "../templates/VWrapper.vue"
import VDashboard from "../organisms/VDashboard.vue"
export default {
  name: "VIndexPage",
  components: {
    VWrapper,
    VDashboard
  }
}
</script>