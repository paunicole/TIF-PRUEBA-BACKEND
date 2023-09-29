USE discord;

INSERT INTO discord.servers (name, description, admin_user) VALUES ('Literatura Fantástica', 'Descripción del servidor 1', 1);
INSERT INTO discord.servers (name, description, admin_user) VALUES ('Programación Web', 'Descripción del servidor 2', 2);
INSERT INTO discord.servers (name, description, admin_user) VALUES ('Peliculas', 'Descripción del servidor 3', 1);
INSERT INTO discord.servers (name, description, admin_user) VALUES ('Upateco', 'Descripción del servidor 4', 2);
INSERT INTO discord.servers (name, description, admin_user) VALUES ('Deportes', 'Descripción del servidor 5', 1);
INSERT INTO discord.servers (name, description, admin_user) VALUES ('Musica', 'Descripción del servidor 6', 2);
INSERT INTO discord.servers (name, description, admin_user) VALUES ('Animes', 'Descripción del servidor 7', 6);
INSERT INTO discord.servers (name, description, admin_user) VALUES ('Comics', 'Descripción del servidor 8', 2);
-- INSERT INTO discord.servers (name, description, admin_user) VALUES ('Cyberpunk: Edgerunners', 'Descripción del servidor 9', 15);
-- INSERT INTO discord.servers (name, description, admin_user) VALUES ('River Plate Fan Club', 'Descripción del servidor 10', 4);
-- INSERT INTO discord.servers (name, description, admin_user) VALUES ('Bocas Junior Fan Club', 'Descripción del servidor 11', 8);
-- INSERT INTO discord.servers (name, description, admin_user) VALUES ('The Wichert', 'Descripción del servidor 12', 4);
-- INSERT INTO discord.servers (name, description, admin_user) VALUES ('GOT Argentina', 'Descripción del servidor 13', 5);
-- INSERT INTO discord.servers (name, description, admin_user) VALUES ('Game Of Thrones', 'Descripción del servidor 14', 4);



INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('ivana@gmail.com', 'ivana', 'ivana123', 'María Ivana', 'Maidana', '2000-01-01', 'avatar1.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('nicole@gmail.com', 'nicole', 'nicole123', 'Paula Nicole', 'Cardozo Gómez', '2000-02-02', 'avatar1.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('beto@gmail.com', 'beto', 'beto123', 'Alberto', 'Pallares', '2000-03-03', 'avatar2.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('pablo@gmail.com', 'pablo', 'pablo123', 'Pablo', 'Rodriguez', '2000-03-03', 'avatar2.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('ivan@gmail.com', 'Ivan', 'Ivana369', 'Ivan', 'Arramayo', '2000-09-01', 'avatar2.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('walter@gmail.com', 'ElProfWalter', 'ElProfeWalter', 'Walter', 'Ramirez', '1984-02-02', 'avatar1.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('Alberto@gmail.com', 'Alberto', 'Alberto123', 'Alberto', 'Tapia', '2000-04-03', 'avatar2.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('Gustavo@gmail.com', 'Gustavo', 'Gustavo123', 'Gustavo', 'Maidana', '2005-01-01', 'avatar1.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('gonzalo@gmail.com', 'gonzalo5', 'gonzalo123', 'Gonzalo', 'Tapia', '2001-02-02', 'avatar1.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('Enrique@gmail.com', 'Enrique', 'Enrique123', 'Enrique', 'Rodriguez', '1995-03-09', 'avatar2.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('Leonel@gmail.com', 'Leonel', 'Leonel123', 'Leonel', 'Rodriguez', '1996-02-11', 'avatar1.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('maria@gmail.com', 'nicole', 'nicole123', 'Paula Nicole', 'Cardozo Gómez', '2000-02-02', 'avatar1.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('Antonela@gmail.com', 'Antonela', 'Antonela123', 'Antonela', 'Tapia', '2000-03-03', 'avatar2.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('David@gmail.com', 'DavidMartinez', 'Martinez2077', 'David', 'Martinez', '2065-09-03', 'avatar2.png');
INSERT INTO discord.users (email, username, password, first_name, last_name, birthdate, avatar) VALUES ('Lucy@gmail.com', 'Lucy', 'Lucy2077', 'Lucyna', 'Kushinada', '2066-03-03', 'avatar2.png');


INSERT INTO discord.server_user (server_id, user_id) VALUES (1, 1);
INSERT INTO discord.server_user (server_id, user_id) VALUES (1, 2);
INSERT INTO discord.server_user (server_id, user_id) VALUES (1, 3);
INSERT INTO discord.server_user (server_id, user_id) VALUES (1, 4);
INSERT INTO discord.server_user (server_id, user_id) VALUES (2, 1);

-- INSERT INTO discord.server_user (server_id, user_id) VALUES (4, 1);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (4, 2);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (4, 3);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (4, 4);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (4, 6);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (4, 5);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (4, 7);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (4, 8);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (4, 9);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (4, 10);


-- INSERT INTO discord.server_user (server_id, user_id) VALUES (9, 4);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (9, 6);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (9, 15);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (9, 16);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (5, 3);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (6, 4);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (7, 5);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (8, 6);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (12, 7);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (10, 8);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (11, 9);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (1, 10);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (1, 11);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (12, 12);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (13, 13);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (13, 14);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (11, 6);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (11, 3);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (10, 4);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (11, 1);

-- INSERT INTO discord.server_user (server_id, user_id) VALUES (10, 8);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (10, 9);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (10, 15);
-- INSERT INTO discord.server_user (server_id, user_id) VALUES (10, 16);
-- Channels
INSERT INTO discord.channels (name, description, server_id) VALUES ('Chat único', 'Para socializar', 1);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Club de lectura', 'Descripción del canal 1', 1);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Escritores Emergentes', 'Descripción del canal 2', 1);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Recomendaciones', 'Descripción del canal 3', 1);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Chat único', 'Para socializar', 2);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Preguntas técnicas', 'Descripción del canal 1', 2);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Proyectos compartidos', 'Descripción del canal 2', 2);
INSERT INTO discord.channels (name, description, server_id) VALUES ('Recursos útiles', 'Descripción del canal 3', 2);
-- Chanes de River
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Chat único', 'Para socializar', 10);
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Procimos Partidos', 'Fixtur', 10);
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Memes', 'Memes', 10);
-- Chanes de boca
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Chat único', 'Para socializar', 11);
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Procimos Partidos', 'Fixtur', 11);
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Memes', 'Memes', 11);
-- Chanes de Cyberpunk 
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Chat único', 'Para socializar', 9);
-- peliculas
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Chat único', 'Para socializar', 3);
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Procimos Estronos', 'Fixtur', 3);
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Memes', 'Memes', 3);
-- Chanes Animes
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Chat único', 'Para socializar', 7);
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Recomendado', 'Fixtur', 7);
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Memes', 'Memes', 7);
-- Chanes Upatecos 
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Chat único', 'Para socializar', 4);
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Trabajo Final', 'Fixtur', 4);
-- INSERT INTO discord.channels (name, description, server_id) VALUES ('Memes', 'Memes', 4);




INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola a todos! Soy nueva', 1, 1);
INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Ivana! ¡Bienvenida!', 2, 1);
INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Nicole! Gracias por la bienvenida.', 1, 1);
INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Saludos, Ivana y Nicole!', 3, 1);
INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¿Como están?', 4, 1);

-- Chat Upateco
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola a todos! Soy el profe walter', 6, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Recordatorio viernes 29 alas 8 se cierra el plazo para el trabajo final', 6, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Nicole! Gracias por la bienvenida.', 2, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('No profe una semanita mas', 3, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('y no jodemos mas', 5, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('x2', 6, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('x3', 7, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('x4', 8, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('No sea rata XD', 9, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Si lo es no ves que fue a la 2', 10, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('XD', 11, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Hola Profe le deje un Easter para ustede guardado. Busquelo XD', 4, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Primera pista', 4, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Con todos los seres y cosas tengo relacion, mas algunos me envitany odian sin compasion.', 4, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Tocame y mirame con deseo, hasta volverte loco, ningun golpe me causa dolor ni me lastima tampoco.', 4, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Los viejos me tienen miedo, los niños gozan conmigo, las bellas doncellas bailan y cantan con regocijo.', 4, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Solloza y llorare, bosteza y dormire y otra sonrisa devolvere.', 4, 22);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Que soy', 4, 22);



-- Chat CyberPunk
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Hola Walter te estaba esperando', 15, 15);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Te estabamos esperando querras decir.', 16, 15);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Para contarte nuestra historia', 16, 15);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Un pajarito me conto que te gustan los animes', 15, 15);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('En tonces nosotros te tenemos uno', 16, 15);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Primero un trailer', 16, 15);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('https://www.youtube.com/watch?v=2CDMfmiXZss&t=74s', 16, 15);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Espero que te juste nuestra historia', 15, 15);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('para cuando lo termines de ver', 16, 15);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('https://www.youtube.com/shorts/dRHLGHoWc04', 16, 15);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Gracias por ver nos ', 16, 15);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('Y nos vemos en la luna', 16, 15);



-- Chat de river plate
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola a todos! Soy nueva', 1, 9);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Ivana! ¡Bienvenida!', 2, 9);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Nicole! Gracias por la bienvenida.', 1, 9);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Saludos, Ivana y Nicole!', 3, 9);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¿Como están?', 4, 9);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola a todos! Soy nueva', 1, 9);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Ivana! ¡Bienvenida!', 2, 9);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Nicole! Gracias por la bienvenida.', 1, 9);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Saludos, Ivana y Nicole!', 3, 9);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¿Como están?', 4, 9);

-- Chat de Boca junior
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola a todos! Soy nueva', 1, 12);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Ivana! ¡Bienvenida!', 2, 12);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Nicole! Gracias por la bienvenida.', 1, 12);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Saludos, Ivana y Nicole!', 3, 12);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¿Como están?', 4, 12);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola a todos! Soy nueva', 1, 13);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Ivana! ¡Bienvenida!', 2, 13);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Hola, Nicole! Gracias por la bienvenida.', 1, 13);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¡Saludos, Ivana y Nicole!', 3, 13);
-- INSERT INTO discord.messages (message, user_id, channel_id) VALUES ('¿Como están?', 4, 13);


-- https://drive.google.com/drive/folders/1ZPdCRZv3zU7KivmlEjngxIK-XA85QgHA?usp=sharing