# test_test

describe directory('/tmp/molecule/inspec/controls') do
  its('owner') { should eq 'root' }
  its('group') { should eq 'root' }
  its('mode') { should cmp '0755' }
end

describe file('/tmp/molecule/inspec/controls/test_test.rb') do
  its('owner') { should eq 'root' }
  its('group') { should eq 'root' }
  its('mode') { should cmp '0644' }
end
