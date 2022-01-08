<template>
<div id="v-reference-task-list">
  <form method="POST" v-on:submit.prevent="nop">
    <table>
      <thead>
        <tr>
          <th>Task Name</th>
          <th>Slot</th>
          <th>Required Effort</th>
          <th>Remaining Time</th>
          <th>Probability</th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="referenceTask in referenceTaskList" v-bind:key="referenceTask.id">
            <td>{{ referenceTask.name }}</td>
            <td>{{ referenceTask.slot }}</td>
            <td>{{ referenceTask.required_effort }}</td>
            <td>{{ referenceTask.remaining_time }}</td>
            <td>{{ referenceTask.P }}</td>
            <td>
              <button
                type="submit"
                v-bind:name="referenceTask.name"
                v-bind:value="referenceTask.name"
                v-on:click="deleteReferenceTask"
              >
                Delete
              </button>
            </td>
            <td>
              <button
                type="submit"
                v-bind:name="referenceTask.name" v-bind:value="referenceTask.name" v-on:click="createTask"
              >
                Create
              </button>
            </td>
        </tr>
      </tbody>
    </table>
  </form>
</div>
</template>

<style lang="scss">
#v-reference-task-list {
  th, td {
    font-size: 20px;
    height: 40px;
    text-align: center;
    width: 200px;
  }
}
</style>

<script>
export default {
  name: "VReferenceTaskList",
  props: {
    referenceTaskList: {
      type: Array,
      default: []
    }
  },
  methods: {
    createTask: function(event) {
      let name = event.target.name
      this.$emit("create-task", {
        name: name
      })
    },
    deleteReferenceTask: function(event) {
      let name = event.target.name
      this.$emit("delete-reference-task", {
        name: name
      })
    }
  }
}
</script>