guard :spork, :cucumber => false, :test_unit => false do
  # reload spec dependencies when any of the watched files change
  watch('spec/spec_helper.rb')
end

guard :rspec do
  # run corresponding spec when app files change
  watch(%r{^app/(.+)\.rb$})        { |m| "spec/app/#{m[1]}_spec.rb" }
  watch(%r{^lib/(.+)\.rb$})        { |m| "spec/lib/#{m[1]}_spec.rb" }

  # run specs when they are changed
  watch(%r{^spec/(.+)_spec\.rb$})
  
  # run everything when spec_helper changes
  watch('spec/spec_helper.rb') { "spec" }
end

guard :bundler do
  watch('Gemfile')
end