<template>
<div id="v-reference-task-list">
  <form method="POST" v-on:submit.prevent="submit">
    <table>
      <thead>
        <tr>
          <th>Task Name</th>
          <th>Required Effort</th>
          <th>Remaining Time</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="referenceTask in referenceTaskList" v-bind:key="referenceTask.id">
            <td>{{ referenceTask.name }}</td>
            <td>{{ referenceTask.required_effort }}</td>
            <td>{{ referenceTask.remaining_time }}</td>
            <td>
              <button type="submit" name="button" v-bind:value="referenceTask.name">Create</button>
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
    submit: function(event) {
      let name = event.target.button.value
      this.$emit("create-task", {
        name: name
      })
    }
  }
}
</script>