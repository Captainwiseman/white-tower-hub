<script>
    import {createEventDispatcher} from 'svelte';
    const dispatch = createEventDispatcher();


    export let active = false
    export let title
    export let tabId
    export let iconClass

   $: liCSSClass = active ? "nav-item active" : "nav-item";
    let changeTab = () => {
        if (active) {
            dispatch("navigationButtonClicked", {
                shouldChangeActiveTab: false,
                shouldRefreshActiveTab: true
            })
        } else {
            // liCSSClass = "nav-item active"
            active = true
            dispatch("navigationButtonClicked", {
                shouldChangeActiveTab: true,
                changeActiveTabTo: tabId
            })
        }
    }
</script>

<li class={liCSSClass}>
    <span class="nav-link" on:click={()=> changeTab()}>
        <i class={iconClass}></i>
        <span>{title}</span>
    </span>
</li>