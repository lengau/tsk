# tell
Tell the user (via desktop notification) when a command completes.

Requires the notify2 package (python3-notify2 on Ubuntu).

## Example Usage
Quick alert for 5 minutes from now:
`tell sleep 300`

Ping machines from a list and fail if one of them is offline.
```
tell 'while read machine;
do
  ping -c 1 $machine || exit 1
done < machines'
```
