# Historial de cambios de la base de conocimiento del CAU del CEPRUD

## 2026-08-05

* **Corrección**: Reparado este registro de cambios, cuyo contenido estaba escapado
  y no era Markdown válido. Se recupera el formato previsto en la especificación OKF.
* **Corrección**: Declarada la versión `okf_version: "0.1"` en el
  [índice general](/index.md). La versión declarada anteriormente no existe.
* **Corrección**: Añadido el campo `type` al [README](/README.md), que como documento
  no reservado debe declararlo.
* **Actualización**: Asignado el tipo `TicketCategory` a las categorías de IRIS que
  llevaban un tipo genérico, y `status: placeholder` a las fichas sin contenido operativo.
* **Actualización**: Enlazadas las referencias a `Sin resolver` que figuraban como texto plano.
* **Actualización**: Añadido el campo `abbreviation` a los espacios docentes.
* **Actualización**: Unificada la denominación de la categoría `Usuario/rol duplicado`.
* **Actualización**: Movidos los scripts a `herramientas/` y añadido `.gitattributes`.
* **Actualización**: Suprimido el tipo genérico `KnowledgeDocument`. Los 30 documentos
  que lo llevaban pasan a `SpaceType` (9), `UserType` (7), `Concept` (6),
  `Governance` (3), `Role` (2), `DecisionTree` (1) y `Procedure` (1).
* **Actualización**: Completados en los 89 documentos los campos `confidentiality`,
  `timestamp` y `review_date`. Se marcan como `restringido` las fichas de
  [vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md) y
  [proveedor de identidad](/prado/conceptos-y-reglas/proveedor-identidad-idp.md).
* **Actualización**: Fijada una revisión mensual (`review_date`) para los diez documentos
  que contienen plazos o calendarios, y trimestral para el resto.
* **Creación**: [Parámetros operativos de PRADO](/prado/parametros-operativos.md) como
  fuente única de plazos, calendarios y ventanas de ejecución.
* **Corrección**: Eliminadas las tres copias del calendario de bajas automáticas
  —en [bajas automáticas](/prado/conceptos-y-reglas/bajas-automaticas.md),
  [vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md) y
  [baja de usuario](/prado/iris/baja-usuario.md)— y las seis declaraciones dispersas de
  los plazos de 24 y 48 horas. Todas remiten ahora al documento de parámetros.
  Se conservan los valores literales dentro de las plantillas de respuesta, porque su
  texto se envía tal cual a la persona usuaria.
* **Actualización**: Añadida a la
  [guía de revisión y mantenimiento](/guia-revision-mantenimiento.md) la regla de fuente
  única para los valores volátiles.
* **Creación**: Carpeta [respuestas tipo](/respuestas-tipo/index.md) con las tres primeras
  respuestas normalizadas (RT-001 a RT-003), extraídas de la regla y de la categoría de
  incidencia administrativa, donde estaban duplicadas con redacciones divergentes.
* **Corrección**: Desduplicado el par
  [regla](/prado/conceptos-y-reglas/incidencia-administrativa.md) /
  [categoría de IRIS](/prado/iris/incidencia-administrativa.md) de incidencia
  administrativa. La regla conserva la definición y el comportamiento del sistema; la
  categoría conserva solo los criterios de clasificación; el texto de respuesta pasa a las
  fichas RT. La categoría cambia su título a `IRIS: Incidencia administrativa` para dejar
  de ser indistinguible de la regla en la recuperación.
* **Creación**: Respuestas tipo RT-004 a RT-006, extraídas del par
  [bajas automáticas](/prado/conceptos-y-reglas/bajas-automaticas.md) /
  [baja de usuario](/prado/iris/baja-usuario.md), donde el mismo texto figuraba con dos
  redacciones ligeramente distintas.
* **Actualización**: Prefijadas con `IRIS: ` las nueve categorías que tenían un documento
  de contrapartida, y añadido en cada una un aviso de alcance que delega la definición del
  fenómeno y el texto de respuesta en los documentos correspondientes. Se añade el campo
  `regla_aplicable` para hacer explícita la relación en el frontmatter.
* **Corrección**: Dividido el
  [árbol general de decisión](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md)
  en un tronco y cinco ramas independientes. Cada rama declara en su primer párrafo la
  condición que lleva hasta ella, de modo que sea comprensible de forma aislada. Se
  eliminan las anclas internas y se añade un diagrama Mermaid.
* **Corrección**: Rebajados a nivel 2 los encabezados de las fases del
  [flujo general de resolución](/prado/arquitectura-y-procesos/flujo-general-resolucion-incidencias.md),
  que usaba ocho encabezados de nivel 1 en un mismo documento.
* **Creación**: Primer contenido operativo de [ABIERTA UGR](/abierta/index.md): concepto de
  MOOC, reglas de certificados y tasas, bonificaciones, plazos y evaluación, tres
  procedimientos y las respuestas tipo RT-101 a RT-117.
* **Creación**: Primer contenido operativo de [e-Campus](/ecampus/index.md): concepto de
  plataforma, regla de competencia del CAU y respuestas tipo RT-201 a RT-204.
* **Nota**: El material procede de las respuestas reales utilizadas por el CAU. Se han
  eliminado los nombres de personas usuarias, las fechas concretas, las denominaciones de
  cursos y ediciones y los enlaces con token de descarga que figuraban en la fuente.
* **Actualización**: Migrados los **1.505 enlaces internos** a la forma absoluta de bundle
  que recomienda la §5.1 de OKF. Ya no hay ningún enlace relativo. Con ello, mover un
  documento de carpeta deja de romper enlaces.
* **Corrección**: Corregido el validador v1, que resolvía los enlaces absolutos fuera del
  repositorio y por tanto penalizaba la forma recomendada por la especificación.
* **Corrección**: Dos entradas de índice enlazaban a
  [IRIS: Usuario/rol duplicado](/prado/iris/usuario-rol-duplicado.md) con el título de otro
  documento. Corregidas.
* **Actualización**: Normalizadas las etiquetas de enlace en listas y tablas y recortadas a
  seis las etiquetas de los nueve documentos que excedían el máximo.
* **Creación**: Materiales de la auditoría OKF en `_auditoria-2026-08/`.

* **Corrección**: Resuelta la contradicción sobre la categoría
  [Sin resolver](/prado/iris/sin-resolver.md). La ficha negaba que existieran criterios de
  selección mientras veinte documentos los aplicaban. Se eleva a la ficha el criterio que
  ya se venía usando de forma coherente, marcado expresamente como síntesis operativa
  pendiente de validación institucional.

* **Actualización**: Asignada `FOL` como unidad responsable (`owner`) de los 90 documentos
  del bundle. Sustituye a los valores `por-definir` y a las asignaciones nominales a
  personas, conforme al criterio de que el responsable sea una unidad y no un individuo.

## 2026-08-04

* **Actualización**: Incorporada la validación automática mediante GitHub Actions.
* **Actualización**: Añadido el distintivo de estado de la validación al [README](/README.md).

## 2026-08-03

* **Inicialización**: Creada la estructura principal del repositorio y el
  [índice general](/index.md).
* **Creación**: Estructura de [PRADO](/prado/index.md) con las categorías de
  [espacios docentes](/prado/espacios-docentes/index.md),
  [usuarios y roles](/prado/usuarios-y-roles/index.md),
  [conceptos y reglas](/prado/conceptos-y-reglas/index.md),
  [procedimientos y casuísticas](/prado/procedimientos/index.md) y
  [clasificación de tickets en IRIS](/prado/iris/index.md).
* **Creación**: Procedimiento
  [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md),
  con comprobaciones, árbol de decisión y plantillas de respuesta.
* **Creación**: Categoría de IRIS
  [Ordenación docente](/prado/iris/ordenacion-docente.md), enlazada con el procedimiento
  sobre asignaturas o grupos no visibles para el profesorado.
