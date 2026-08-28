local stringify = pandoc.utils.stringify

local function plain_inlines(text)
  return pandoc.Inlines({pandoc.Str(text)})
end

local function normalized_header(header)
  local title = stringify(header.content)
  local appendix_title = title:match("^Appendix%s+[A-Z]%.%s*(.+)$")
  if appendix_title then
    header.content = plain_inlines(appendix_title)
    header.level = math.max(1, header.level - 1)
    header.identifier = ""
    return {pandoc.RawBlock("latex", "\\appendix"), header}
  end

  title = title:gsub("^%d+%.%d+%.%s*", "")
  title = title:gsub("^%d+%.%s*", "")
  header.content = plain_inlines(title)
  header.level = math.max(1, header.level - 1)
  header.identifier = ""
  if title == "References" then
    header.classes = {"unnumbered"}
  end
  return {header}
end

function Pandoc(document)
  local source = document.blocks
  local output = pandoc.Blocks({})
  local index = 1
  local candidate_version = stringify(document.meta.candidate_version or "")

  if source[index] and source[index].tag == "Header" and source[index].level == 1 then
    index = index + 1
  end
  if source[index] and source[index].tag == "Para" then
    local metadata_line = stringify(source[index])
    if metadata_line:match("^Candidate research manuscript") then
      index = index + 1
    end
  end

  output:insert(pandoc.RawBlock(
    "latex",
    "\\begin{center}\\small " ..
    "\\textbf{Candidate version:} " .. candidate_version .. "\\\\ " ..
    "\\textbf{Assurance:} unrefereed theorem candidate with deterministic " ..
    "internal replay; no independent specialist review or submission.\\\\ " ..
    "\\textbf{Artifact identity:} bound by \\texttt{PACKAGE\\_MANIFEST.json}; " ..
    "component licences are recorded in \\texttt{LICENSES.md}; public archive " ..
    "identifier, DOI and release URL are pending publisher packaging." ..
    "\\end{center}"
  ))

  while index <= #source do
    local block = source[index]
    if block.tag == "Header" and stringify(block.content) == "Abstract" then
      output:insert(pandoc.RawBlock("latex", "\\begin{abstract}"))
      index = index + 1
      while index <= #source do
        local abstract_block = source[index]
        if abstract_block.tag == "Header" and abstract_block.level <= 2 then
          break
        end
        output:insert(abstract_block)
        index = index + 1
      end
      output:insert(pandoc.RawBlock("latex", "\\end{abstract}"))
      output:insert(pandoc.RawBlock(
        "latex",
        "\\noindent\\textbf{Keywords:} polynomial exponential periods; " ..
        "twisted de Rham modules; inverse-at-infinity support; Dickson " ..
        "polynomials; polynomial monodromy; creative telescoping; " ..
        "zero-cycles; Bautin ideals; Melnikov functions."
      ))
    elseif block.tag == "Header" then
      for _, normalized in ipairs(normalized_header(block)) do
        output:insert(normalized)
      end
      index = index + 1
    else
      output:insert(block)
      index = index + 1
    end
  end

  document.blocks = output
  return document
end
