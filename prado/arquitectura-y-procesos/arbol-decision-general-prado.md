---
type: KnowledgeDocument
title: Árbol general de decisión para incidencias de PRADO
description: Árbol operativo para orientar la clasificación y las comprobaciones iniciales de una incidencia de PRADO.
service: PRADO
status: draft
language: es
last_reviewed: 2026-08-03
tags:
  - prado
  - arquitectura
  - procesos
  - arbol-decision
  - tickets
---

# Árbol general de decisión para incidencias de PRADO

## Naturaleza de este documento

Este árbol es una **síntesis operativa** elaborada a partir de las reglas, categorías y procedimientos disponibles en la base de conocimiento.

La documentación interna indica que el árbol de decisión anterior está desactualizado. Por tanto, este documento debe considerarse una primera versión revisable.

## Punto de partida

Antes de utilizar el árbol, registrar:

- plataforma;
- curso académico;
- identidad y correo de la persona;
- condición de alumno, docente, coordinación o usuario externo;
- nombre y código del espacio;
- mensaje de error o comportamiento observado.

# Árbol de decisión

## 1. ¿La persona puede entrar en la plataforma?

### No

Continuar en:

- [Rama A: problemas de acceso](#rama-a-problemas-de-acceso)

### Sí

Pasar a la pregunta 2.

---

## 2. ¿La persona ve el espacio o curso afectado?

### No

Pasar a la pregunta 3.

### Sí

Pasar a la pregunta 6.

---

## 3. ¿La persona debe aparecer según una fuente oficial?

### Es estudiante

Comprobar:

- matrícula oficial;
- curso académico;
- grupo;
- incidencia administrativa;
- plataforma.

Fuentes:

- Grado: Oficina Virtual y vistas de bases de datos;
- Posgrado: vistas de bases de datos.

### Es docente

Comprobar:

- Plan de Ordenación Docente;
- asignatura;
- grupo;
- créditos;
- plataforma y curso académico.

### Es coordinador o coordinadora

Comprobar:

- registro institucional de la coordinación;
- tipo de espacio de gestión;
- rol esperado.

### No consta en ninguna fuente oficial

Pasar a:

- [Rama E: solicitudes de alta manual](#rama-e-solicitudes-de-alta-manual)

---

## 4. ¿La persona aparece en la fuente oficial?

### No

La causa no está en PRADO.

Actuación:

- indicar qué unidad debe corregir el dato;
- no realizar un alta manual como sustitución permanente;
- clasificar como Matrícula u Ordenación docente según corresponda.

### Sí

Pasar a la pregunta 5.

---

## 5. ¿Ha transcurrido el plazo normal de actualización?

### No

Actuación:

- informar del plazo;
- registrar la fecha del cambio;
- esperar a la ejecución del automatismo;
- no duplicar la participación manualmente.

### Sí

Comprobar:

- altas automáticas;
- estado suspendido o no activo;
- cuenta duplicada;
- código y grupo;
- visibilidad;
- plataforma y curso académico.

Continuar en la rama correspondiente:

- [Rama B: alumnado que no ve un curso](#rama-b-alumnado-que-no-ve-un-curso)
- [Rama C: profesorado que no ve una asignatura](#rama-c-profesorado-que-no-ve-una-asignatura)
- [Rama D: espacio oculto o problema de visibilidad](#rama-d-espacio-oculto-o-problema-de-visibilidad)

---

## 6. ¿El problema afecta al rol o a la participación?

### Rol incorrecto o doble rol

Comprobar:

- rol actual;
- rol esperado;
- participaciones duplicadas;
- tipo de espacio;
- fuente o autorización que justifica el rol.

Clasificación habitual:

- Usuario o rol duplicado;
- Gestión manual;
- Ordenación docente.

### Participación suspendida

Comprobar si la persona ha dejado de llegar desde la fuente oficial.

Consultar:

- [Participación suspendida](../usuarios-y-roles/participacion-suspendida.md)

### Participación no activa

Comprobar si fue incorporada manualmente al margen de las bases de datos.

Consultar:

- [Participación no activa](../usuarios-y-roles/participacion-no-activa.md)

### El rol y la participación son correctos

Pasar a la pregunta 7.

---

## 7. ¿El problema está relacionado con la configuración del curso?

### Sí

Clasificar según el caso:

- Visibilidad;
- LMS: Calificaciones;
- LMS: Cuestionarios;
- LMS: Copias `.mbz`;
- LMS: Mensajería y foros;
- LMS: Turnitin;
- LMS: Uso general;
- otra categoría LMS disponible.

### No

Pasar a la pregunta 8.

---

## 8. ¿Se solicita crear o modificar un espacio docente?

### Sí

Comprobar:

- tipo de espacio;
- requisitos de creación;
- código;
- responsables;
- participantes automáticos;
- autorización;
- limitaciones aplicables.

Consultar:

- [Espacios docentes](../espacios-docentes/index.md)

### No

Pasar a la pregunta 9.

---

## 9. ¿La incidencia puede resolverse desde el CEPRUD?

### Sí

Aplicar el procedimiento correspondiente y documentar:

- fuente consultada;
- resultado;
- actuación;
- respuesta facilitada.

### No

Pasar a la pregunta 10.

---

## 10. ¿Existe una unidad competente disponible en IRIS?

### Sí

Valorar la transferencia únicamente después de realizar las comprobaciones.

Consultar:

- [Transferencia de tickets en IRIS](../conceptos-y-reglas/transferencia-tickets-iris.md)

### No

Actuación:

- informar a la persona de la unidad con la que debe contactar;
- dejar constancia de la comprobación;
- cerrar el ticket cuando proceda.

# Rama A: problemas de acceso

## A1. ¿Es un problema de autenticación?

Comprobar:

- cuenta utilizada;
- dominio del correo;
- proveedor de identidad;
- contraseña;
- verificación en dos pasos;
- tipo de usuario.

Consultar:

- [Problemas de acceso con verificación en dos pasos](../procedimientos/problemas-acceso-verificacion-dos-pasos.md)
- [Acceso de docente externo](../procedimientos/acceso-docente-externo.md)

## A2. ¿Existe incidencia administrativa?

### Sí

Clasificar como:

- Incidencia administrativa.

Comprobar:

- Oficina Virtual;
- atributo del IdP;
- caché de acceso;
- unidad o unidades del centro que aparecen.

### No

Continuar con:

- comprobación del IdP;
- perfil de usuario;
- cuenta duplicada;
- plataforma correcta.

## A3. ¿La persona es un usuario manual?

### Sí

Comprobar:

- método de identificación `Cuentas manuales`;
- credenciales propias;
- imposibilidad de acceso mediante SAML.

### No

Continuar con la cuenta institucional.

# Rama B: alumnado que no ve un curso

## B1. ¿La matrícula figura oficialmente?

### No

Indicar que debe resolver la matrícula con la secretaría del centro.

### Sí

Comprobar:

- curso académico;
- grupo;
- incidencia administrativa;
- plazo de sincronización;
- estado de participación;
- visibilidad.

## B2. ¿La participación está suspendida o no activa?

Aplicar la ficha correspondiente.

## B3. ¿El curso está oculto?

Clasificar como:

- Visibilidad.

## B4. ¿El curso está archivado en el área personal?

Indicar cómo localizarlo en las vistas de cursos futuros, en progreso o pasados.

# Rama C: profesorado que no ve una asignatura

## C1. ¿Figura en el POD?

### No

Indicar que la asignación debe corregirse en la unidad responsable.

### Sí

Comprobar:

- grupo;
- créditos;
- curso académico;
- plataforma;
- plazo de actualización;
- estado de la participación.

## C2. ¿Solo tiene créditos prácticos?

### Sí

Comprobar el grupo `SG` y consultar:

- [Docente con solo créditos prácticos](../usuarios-y-roles/docente-creditos-practicos.md)
- [Alta manual de docente con créditos prácticos](../procedimientos/alta-manual-docente-creditos-practicos.md)

## C3. ¿Se solicita un alta sin asignación oficial?

Comprobar si existe:

- autorización de Ordenación Académica;
- ticket transferido y devuelto con el visto bueno;
- supuesto documentado de gestión manual.

# Rama D: espacio oculto o problema de visibilidad

## D1. ¿La persona está correctamente incorporada?

### No

Volver a la rama de matrícula, ordenación docente o gestión manual.

### Sí

Comprobar:

- visibilidad del curso;
- fecha de inicio;
- configuración realizada por el docente;
- archivo en el área personal;
- rol y estado de participación.

Clasificación:

- [Visibilidad](../iris/visibilidad.md)

# Rama E: solicitudes de alta manual

## E1. ¿Existe un supuesto documentado?

Ejemplos:

- docente con créditos prácticos sin grupo;
- alta autorizada por Ordenación Académica;
- persona sin docencia que necesita un EDPP para formación;
- incorporación justificada en un espacio de gestión.

### No

No realizar el alta.

### Sí

Comprobar:

- identidad;
- cuenta institucional;
- rol;
- espacio;
- autorización;
- riesgo de duplicidad;
- responsabilidad sobre la participación.

## E2. ¿Se pretende matricular manualmente a un estudiante?

Advertir que:

- no es la vía recomendada;
- puede terminar como participación no activa;
- no sustituye la matrícula oficial.

Consultar:

- [Matrícula manual](../conceptos-y-reglas/matricula-manual.md)

# Resultado final

Toda rama debe terminar en una de estas decisiones:

```text
Resolver técnicamente
Informar y esperar actualización
Solicitar corrección administrativa
Realizar actuación manual autorizada
Transferir a la unidad competente
Cerrar con información y comprobaciones documentadas
```

## Registro mínimo del ticket

Antes del cierre o la transferencia, dejar anotado:

- plataforma;
- curso académico;
- persona y correo;
- espacio y código;
- fuente consultada;
- dato encontrado;
- plazo comprobado;
- categoría de IRIS;
- actuación realizada;
- resultado final.
