from storage_module.template_dao import TemplateDao
import json

dao = TemplateDao()

document="""{
    "key":"landslide",
    "sessions":[
        {
            "key": "s1",
            "questions": [{
                    "id": "moradores",
                    "label": "Nome de moradores.",
                    "name": "moradores",
                    "required": false,
                    "type": "INPUT",
                    "inputType": "text"
                },
                {
                    "id": "condicoes_acesso",
                    "label": "Condições de acesso à área.",
                    "name": "condicoes_acesso",
                    "required": false,
                    "type": "INPUT",
                    "inputType": "text"
                },
                {
                    "id": "tipo_moradia",
                    "label": "Tipos de moradias.",
                    "name": "tipo_moradia",
                    "options": [{
                            "label": "Alvenaria",
                            "value": "option-1"
                        },
                        {
                            "label": "Madeira",
                            "value": "option-2"
                        },
                        {
                            "label": "Misto (alvenaria e madeira)",
                            "value": "option-3"
                        }
                    ],
                    "type": "RADIO_GROUP"
                }
            ]
        }, {
            "key": "s2",
            "questions": [{
                    "id": "altura_encosta",
                    "label": "Altura da encosta natural (metros).",
                    "name": "altura_encosta",
                    "autoFocus": true,
                    "maxLength": 2,
                    "type": "INPUT",
                    "inputType": "number"
                },
                {
                    "id": "inclinacao_encosta",
                    "label": "Inclinação da encosta natural (graus).",
                    "name": "inclinacao_encosta",
                    "options": [{
                            "label": "90°",
                            "value": "90"
                        },
                        {
                            "label": "60°",
                            "value": "60"
                        },
                        {
                            "label": "30°",
                            "value": "30"
                        },
                        {
                            "label": "17°",
                            "value": "17"
                        },
                        {
                            "label": "10°",
                            "value": "10"
                        }
                    ],
                    "type": "RADIO_GROUP"
                },
                {
                    "id": "altura_talude",
                    "label": "Altura do talude de corte, se existir (metros).",
                    "name": "altura_talude",
                    "maxLength": 2,
                    "type": "INPUT",
                    "inputType": "number"
                },
                {
                    "id": "inclinacao_talude",
                    "label": "Inclinação do talude de corte, se existir (graus).",
                    "name": "inclinacao_talude",
                    "options": [{
                            "label": "90°",
                            "value": "90"
                        },
                        {
                            "label": "60°",
                            "value": "60"
                        },
                        {
                            "label": "30°",
                            "value": "30"
                        },
                        {
                            "label": "17°",
                            "value": "17"
                        },
                        {
                            "label": "10°",
                            "value": "10"
                        }
                    ],
                    "type": "RADIO_GROUP"
                },
                {
                    "id": "distancia_base_talude",
                    "label": "Distância entre as moradias e a base da encosta/talude, se existir (metros).",
                    "name": "distancia_base_talude",
                    "autoFocus": true,
                    "maxLength": 2,
                    "type": "INPUT",
                    "inputType": "number"
                },
                {
                    "id": "distancia_topo_talude",
                    "label": "Distância entre as moradias e o topo da encosta/talude, se existir (metros).",
                    "name": "distancia_topo_talude",
                    "autoFocus": true,
                    "maxLength": 2,
                    "type": "INPUT",
                    "inputType": "number"
                },
                {
                    "id": "altura_aterro",
                    "label": "Altura do aterro lançado, se existir (metros).",
                    "name": "altura_aterro",
                    "autoFocus": true,
                    "maxLength": 2,
                    "type": "INPUT",
                    "inputType": "number"
                },
                {
                    "id": "inclinacao_aterro",
                    "label": "Inclinação do aterro lançado, se existir (graus).",
                    "name": "inclinacao_aterro",
                    "options": [{
                            "label": "90°",
                            "value": "90"
                        },
                        {
                            "label": "60°",
                            "value": "60"
                        },
                        {
                            "label": "30°",
                            "value": "30"
                        },
                        {
                            "label": "17°",
                            "value": "17"
                        },
                        {
                            "label": "10°",
                            "value": "10"
                        }
                    ],
                    "type": "RADIO_GROUP"
                },
                {
                    "id": "distancia_base_aterro",
                    "label": "Distância entre as moradias e a base do aterro (metros).",
                    "name": "distancia_base_aterro",
                    "autoFocus": true,
                    "maxLength": 2,
                    "type": "INPUT",
                    "inputType": "number"
                },
                {
                    "id": "distancia_topo_aterro",
                    "label": "Distância entre as moradias e o topo do aterro (metros).",
                    "name": "distancia_topo_aterro",
                    "autoFocus": true,
                    "maxLength": 2,
                    "type": "INPUT",
                    "inputType": "number"
                },
                {
                    "id": "altura_parede_rochosa",
                    "label": "Altura da parede rochosa, se existir. (metros).",
                    "name": "altura_parede_rochosa",
                    "autoFocus": true,
                    "maxLength": 2,
                    "type": "INPUT",
                    "inputType": "number"
                },
                {
                    "id": "inclinacao_parede_rochosa",
                    "label": "Inclinação da parede rochosa (graus).",
                    "name": "inclinacao_parede_rochosa",
                    "options": [{
                            "label": "90°",
                            "value": "90"
                        },
                        {
                            "label": "60°",
                            "value": "60"
                        },
                        {
                            "label": "30°",
                            "value": "30"
                        },
                        {
                            "label": "17°",
                            "value": "17"
                        },
                        {
                            "label": "10°",
                            "value": "10"
                        }
                    ],
                    "type": "RADIO_GROUP"
                },
                {
                    "id": "presenca_outros",
                    "label": "Há presença de blocos de rocha e matações ou presença de lixo/entulho? Marque se houver.",
                    "name": "presenca_outros",
                    "multiple": true,
                    "type": "SELECT",
                    "options": [{
                            "label": "Blocos de rochas e matações",
                            "value": "option-1"
                        },
                        {
                            "label": "Lixo/entulho",
                            "value": "option-2"
                        }
                    ]
                }
            ]
        }, {
            "key": "s3",
            "questions": [{
                    "id": "drenagem",
                    "label": "Sistema de drenagem superficial.",
                    "name": "drenagem",
                    "type": "RADIO_GROUP",
                    "options": [{
                            "label": "Inexistente",
                            "value": "option-1"
                        },
                        {
                            "label": "Precário",
                            "value": "option-2"
                        },
                        {
                            "label": "Satisfatório",
                            "value": "option-3"
                        }
                    ]
                },
                {
                    "id": "destino_esgoto",
                    "label": "Para onde vai o esgoto?",
                    "name": "destino_esgoto",
                    "type": "RADIO_GROUP",
                    "options": [{
                            "label": "Fossa",
                            "value": "option-1"
                        },
                        {
                            "label": "Canalizado",
                            "value": "option-2"
                        },
                        {
                            "label": "Lançado em superfície (céu aberto)",
                            "value": "option-3"
                        }
                    ]
                },
                {
                    "id": "origem_agua",
                    "label": "De onde vem a água para uso na moradia?",
                    "name": "origem_agua",
                    "type": "RADIO_GROUP",
                    "options": [{
                            "label": "Prefeitura/Concessionária",
                            "value": "option-1"
                        },
                        {
                            "label": "Mangueira",
                            "value": "option-2"
                        }
                    ]
                },
                {
                    "id": "vazamento_tubulacao",
                    "label": "Existe vazamento na tubulação?",
                    "name": "vazamento_tubulacao",
                    "type": "RADIO_GROUP",
                    "options": [{
                            "label": "Sim (esgoto)",
                            "value": "option-1"
                        },
                        {
                            "label": "Sim (água)",
                            "value": "option-2"
                        },
                        {
                            "label": "Não",
                            "value": "option-3"
                        }
                    ]
                },
                {
                    "id": "minas_dagua",
                    "label": "Minas d'água no barranco (talude)",
                    "name": "minas_dagua",
                    "type": "RADIO_GROUP",
                    "options": [{
                            "label": "No pé",
                            "value": "option-1"
                        },
                        {
                            "label": "No meio",
                            "value": "option-2"
                        },
                        {
                            "label": "No topo do talude ou aterro",
                            "value": "option-3"
                        }
                    ]
                }
            ]
        }, {
            "key": "s4",
            "questions": [{
                    "id": "ha_arvores",
                    "label": "Presença de árvores?",
                    "name": "ha_arvores",
                    "type": "CHECKBOX"
                },
                {
                    "id": "desmatamento",
                    "label": "A área foi desmatada?",
                    "name": "desmatamento",
                    "type": "CHECKBOX"
                },
                {
                    "id": "vegetacao_rasteira",
                    "label": "Predominio de vegetação rasteira (arbustos, capim, etc)?",
                    "name": "vegetacao_rasteira",
                    "type": "CHECKBOX"
                },
                {
                    "id": "area_cultivo",
                    "label": "É área de cultivo? Se sim, descreva qual.",
                    "name": "area_cultivo",
                    "type": "CHECKBOX"
                },
                {
                    "id": "tipo_cultivo",
                    "label": "Descrição do cultivo se houver.",
                    "name": "tipo_cultivo",
                    "autoComplete": "on",
                    "maxLength": 60,
                    "placeholder": "Ex.: Banana",
                    "type": "INPUT",
                    "inputType": "text"
                }
            ]
        }, {
            "key": "s5",
            "questions": [{
                    "id": "sinais_trincas",
                    "label": "Existência de trincas",
                    "name": "sinais_trincas",
                    "multiple": true,
                    "type": "SELECT",
                    "options": [{
                            "label": "No terreno",
                            "value": "terreno"
                        },
                        {
                            "label": "Na moradia",
                            "value": "moradia"
                        }
                    ]
                },
                {
                    "id": "sinais_inclinacao",
                    "label": "Existência de sinais de inclinação",
                    "name": "sinais_inclinacao",
                    "multiple": true,
                    "type": "SELECT",
                    "options": [{
                            "label": "Árvores",
                            "value": "arvores"
                        },
                        {
                            "label": "Postes",
                            "value": "postes"
                        },
                        {
                            "label": "Muros",
                            "value": "muros"
                        }
                    ]
                },
                {
                    "id": "sinais_degraus",
                    "label": "Existência de degraus de abatimento?",
                    "name": "sinais_degraus",
                    "type": "CHECKBOX"
                },
                {
                    "id": "sinais_embarrigados",
                    "label": "Existência de muros/paredes 'embarrigados'?",
                    "name": "sinais_embarrigados",
                    "type": "CHECKBOX"
                },
                {
                    "id": "sinais_cicatriz",
                    "label": "Existência de cicatriz de escorregamento próxima à moradia?",
                    "name": "sinais_cicatriz",
                    "type": "CHECKBOX"
                }
            ]
        }, {
            "key": "s6",
            "questions": [{
                    "id": "instabilizacao_escorregamento",
                    "label": "Existência de processo de instabilização, esperado ou já ocorrido, relacionado a escorregamentos:",
                    "name": "instabilizacao_escorregamento",
                    "multiple": true,
                    "type": "SELECT",
                    "options": [{
                            "label": "No talude natural",
                            "value": "talude_natural"
                        },
                        {
                            "label": "No talude de corte",
                            "value": "talude_corte"
                        },
                        {
                            "label": "No aterro",
                            "value": "aterro"
                        }
                    ]
                },
                {
                    "id": "instabilizacao_queda_blocos",
                    "label": "Existência de processo de instabilização, esperado ou já ocorrido, relacionado a Queda de Blocos?",
                    "name": "instabilizacao_queda_blocos",
                    "type": "CHECKBOX"
                },
                {
                    "id": "instabilizacao_rolamento_blocos",
                    "label": "Existência de processo de instabilização, esperado ou já ocorrido, relacionado a Rolamento de Blocos?",
                    "name": "instabilizacao_rolamento_blocos",
                    "type": "CHECKBOX"
                }
            ]
        }, {
            "key": "s7",
            "questions": [{
                "id": "grau_risco",
                "label": "Em sua avaliação qual é o grau de risco desta ocorrência?",
                "name": "grau_risco",
                "type": "RADIO_GROUP",
                "options": [{
                        "label": "Muito alto (Providência imediata)",
                        "value": "option-1"
                    },
                    {
                        "label": "Alto (Manter local em observação)",
                        "value": "option-2"
                    },
                    {
                        "label": "Médio (Manter local em observação)",
                        "value": "option-3"
                    },
                    {
                        "label": "Baixo ou inexistente (Pode incluir situações sem risco)",
                        "value": "option-3"
                    }
                ]
            }]
        }, {
            "key": "s8",
            "questions": [{
                    "id": "moradias_risco",
                    "label": "Número de moradias em risco.",
                    "name": "moradias_risco",
                    "type": "INPUT",
                    "inputType": "number"
                },
                {
                    "id": "pessoas_remocao",
                    "label": "Estimativa do número de pessoas para remoção.",
                    "name": "pessoas_remocao",
                    "type": "INPUT",
                    "inputType": "number"
                }
            ]
        }, {
            "key": "s9",
            "questions": [{
                    "id": "outras_informacoes",
                    "label": "Escreva neste espaço quaisquer informações adicionais que você julgar importante.",
                    "name": "outras_informacoes",
                    "autoComplete": "on",
                    "autoFocus": true,
                    "type": "TEXTAREA",
                    "cols": 20,
                    "rows": 12,
                    "wrap": "soft"
                },
                {
                    "id": "equipe",
                    "label": "Equipe técnica (nome/instituição).",
                    "name": "equipe",
                    "autoComplete": "on",
                    "maxLength": 60,
                    "type": "INPUT",
                    "inputType": "text"
                },
                {
                    "id": "numero_ocorrencia",
                    "label": "Código da vistoria.",
                    "name": "numero_ocorrencia",
                    "readOnly": true,
                    "type": "INPUT",
                    "inputType": "number"
                }
            ]
        }
    ]}"""
jsonDoc=json.loads(document)
dao.addTemplateSession(jsonDoc)

document="""{
    "key":"default",
    "sessions":[
      {
        "key":"s1",
        "questions":[{
          "id":"natureza",
          "label":"Natureza da ocorrência.",
          "name":"natureza",
          "options":[
             {
                "disabled":false,
                "label":"Colmeia de abelhas",
                "value":"option-1"
             },
             {
                "disabled":false,
                "label":"Padrão de luz",
                "value":"option-2"
             },
             {
                "disabled":false,
                "label":"Queda de árvore",
                "value":"option-3"
             }
          ],
          "type":"RADIO_GROUP"
        },
        {
          "id":"numero_ocorrencia",
          "label":"Código da vistoria.",
          "name":"numero_ocorrencia",
          "value":"",
          "readOnly":true,
          "required":false,
          "type":"INPUT",
          "inputType":"text"
        }]
      },
      {
        "key":"s2",
        "questions":[{
          "id":"solicitante",
          "label":"Solicitante (pode ser um orgão ou pessoa)",
          "name":"solicitante",
          "validators": {
            "required":null,
            "minLength": 1
          },
          "autoComplete":"on",
          "autoFocus":true,
          "maxLength":60,
          "placeholder":"Ex.: SEMMA",
          "type":"INPUT",
          "inputType":"text"
        },
        {
          "id":"cpf_rg",
          "label":"CPF ou RG do solicitante, apenas números.",
          "name":"cpf_rg",
          "autoComplete":"on",
          "autoFocus":true,
          "maxLength":60,
          "placeholder":"Digite CPF ou RG",
          "type":"INPUT",
          "inputType":"number"
        },
        {
          "id":"telefone",
          "label":"Telefone para contato, apenas números. Pode incluir DDD.",
          "name":"telefone",
          "autoFocus":true,
          "maxLength":12,
          "placeholder":"11998010101",
          "type":"INPUT",
          "inputType":"number"
        }]
      },
      {
        "key":"s3",
        "questions":[{  
              "id":"data_oco",
              "label":"Data da ocorrência.",
              "name":"data_oco",
              "type":"DATEPICKER",
              "required": false,
              "inline":false,
              "format":"DD/MM/YYYY",
              "additional": {
                "pickerFormat": "D MMM, YYYY",
                "monthShortNames" : ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
              }
            },
            {  
              "id":"hora_oco",
              "label":"Hora da ocorrência.",
              "name":"hora_oco",
              "type":"TIMEPICKER",
              "required": false,
              "inline":false,
              "format":"HH:mm",
              "additional": {
                "pickerFormat": "HH:mm"
              }
            },
            {  
              "id":"hora_local",
              "label":"Hora da chegada ao local.",
              "name":"hora_local",
              "type":"TIMEPICKER",
              "validators": {
                "required":null
              },
              "inline":false,
              "format":"HH:mm",
              "additional": {
                "pickerFormat": "HH:mm"
              }
            }
        ]
      },
      {
        "key":"s4",
        "questions":[{
          "id":"descricao",
          "label":"Descrição da ocorrência.",
          "name":"descricao",
          "validators": {
            "required":null,
            "minLength": 1
          },
          "autoComplete":"on",
          "autoFocus":true,
          "type":"TEXTAREA",
          "cols":20,
          "rows":12,
          "wrap":"soft"
        },
        {
          "id":"causa",
          "label":"Descrição das causas, conhecidas ou prováveis, da ocorrência.",
          "name":"causa",
          "validators": {
            "required":null,
            "minLength": 1
          },
          "autoComplete":"on",
          "autoFocus":true,
          "maxLength":60,
          "placeholder":"Fortes chuvas...",
          "type":"INPUT",
          "inputType":"text"
       }]
      },
      {
        "key":"s5",
        "questions":[{
          "id":"parecer",
          "label":"Descrição do parecer da Defesa Civil.",
          "name":"parecer",
          "validators": {
            "required":null,
            "minLength": 1
          },
          "autoComplete":"on",
          "autoFocus":true,
          "maxLength":60,
          "placeholder":"Ex.: Supressão da árvore",
          "type":"INPUT",
          "inputType":"text"
        },
        {
          "id":"grau_risco",
          "label":"Em sua avaliação qual é o grau de risco desta ocorrência?",
          "name":"grau_risco",
          "options":[
            {
                "label":"Baixo",
                "value":"option-1"
            },
            {
                "label":"Médio",
                "value":"option-2"
            },
            {
                "label":"Alto",
                "value":"option-3"
            }
          ],
          "type":"RADIO_GROUP"
        },
        {
          "id":"cc",
          "label":"Este documento deverá ser enviado para:",
          "name":"cc",
          "multiple": true,
          "type":"SELECT",
          "options":[
            {  
              "label":"SEMMA",
              "value":"semma"
            },
            {  
              "label":"SSM",
              "value":"ssm"
            },
            {  
              "label":"URBAM",
              "value":"urbam"
            },
            {  
              "label":"Gabinete",
              "value":"gabinete"
            }
          ]
        },
        {
          "id":"outros",
          "label":"Outros utilizados.",
          "name":"outros",
          "autoComplete":"on",
          "autoFocus":true,
          "maxLength":50,
          "placeholder":"Opcional...",
          "type":"INPUT",
          "inputType":"text"
        }]
      }
    ]}"""
jsonDoc=json.loads(document)
dao.addTemplateSession(jsonDoc)