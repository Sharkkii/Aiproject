<template>
<div id="v-task-panel">
  <div class="sub-header">
    <p>Task Panel</p>
  </div>
  <v-reference-task-list
    v-bind:reference-task-list="referenceTaskList"
    v-on:create-task="createTask"
    v-on:delete-reference-task="deleteReferenceTask"
  >
  </v-reference-task-list>
  <v-reference-task-create-button
    v-on:create-reference-task="createReferenceTask"
  >
  </v-reference-task-create-button>
</div>
</template>

<style scoped lang="scss">
#v-task-panel {
  box-shadow: 0 0 5px $black;
  box-sizing: border-box;
  padding: 20px;
  width: 600px;
}

.sub-header {
  color: $main-color;
  font-size: 30px;
  font-weight: bold;
}
</style>

<script>
import VReferenceTaskList from '../molecules/VReferenceTaskList.vue'
import VReferenceTaskCreateButton from '../molecules/VReferenceTaskCreateButton.vue'
export default {
  name: "VTaskPanel",
  props: {
    referenceTaskList: {
      type: Array,
      default: []
    }
  },
  methods: {
    createReferenceTask: function(data) {
      this.$emit("create-reference-task", data)
    },
    createTask: function(data) {
      this.$emit("create-task", data)
    },
    deleteReferenceTask: function(data) {
      this.$emit("delete-reference-task", data)
    }
  },
  components: {
    VReferenceTaskList, VReferenceTaskCreateButton
  }
}
</script>