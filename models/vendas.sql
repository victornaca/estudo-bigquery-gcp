config {
  type: "view",
  schema: "raw_data",
  name: "vendas_raw"
}

select * from {{ ref("vendas") }};