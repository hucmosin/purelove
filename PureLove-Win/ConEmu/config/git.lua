function git_prompt_filter()
    clink.prompt.value = string.gsub(clink.prompt.value, "{git}", "")
end

clink.prompt.register_filter(git_prompt_filter, 50)
