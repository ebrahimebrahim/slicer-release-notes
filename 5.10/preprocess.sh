notes="${SLICER_RELEASE_NOTES}"
notes_grouped="${SLICER_RELEASE_NOTES_GROUPED}"

declare -A types=(
  ["ENH"]="Improvements"
  ["PERF"]="Performance"
  ["BUG"]="Fixes"
  ["DOC"]="Documentation"
  ["COMP"]="Compilation"
  ["STYLE"]="Style"
)

(
for type in ENH PERF BUG DOC STYLE COMP; do
  echo "#------------------------------------------------------------------------------"
  echo "# ${types[${type}]}"
  echo
  ack "${type}:" "${notes}" \
    | ack -v "@(slicerbot|dependabot|slicer-app)" \
    | sed -E "s/\* ${type}: /\* /"
  echo
done

echo "#------------------------------------------------------------------------------"
echo "# Uncategorized"
echo
ack -v "(ENH|PERF|BUG|DOC|COMP|STYLE):" "${notes}" \
  | ack -v "@(slicerbot|dependabot|slicer-app)"
echo

echo "#------------------------------------------------------------------------------"
echo "# slicerbot"
echo
sed -E "s/\* (ENH|PERF|BUG|DOC|COMP|STYLE): /\* /" "${notes}" \
  | ack "@slicerbot"
echo

echo "#------------------------------------------------------------------------------"
echo "# slicer-app"
echo
sed -E "s/\* (ENH|PERF|BUG|DOC|COMP|STYLE): /\* /" "${notes}" \
  | ack "@slicer-app"
echo

echo "#------------------------------------------------------------------------------"
echo "# dependabot"
echo
ack "@dependabot" "${notes}" \
  | sed -E "s/\* (ENH|PERF|BUG|DOC|COMP|STYLE): /\* /"
echo

) > "${notes_grouped}"
