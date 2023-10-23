CREATE TABLE `role` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(80) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `permissions` text DEFAULT NULL,
  `update_datetime` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE `roles_users` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE `user` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `fs_uniquifier` varchar(64) NOT NULL,
  `confirmed_at` timestamp NULL DEFAULT NULL,
  `last_login_at` timestamp NULL DEFAULT NULL,
  `current_login_at` timestamp NULL DEFAULT NULL,
  `last_login_ip` varchar(64) DEFAULT NULL,
  `current_login_ip` varchar(64) DEFAULT NULL,
  `login_count` int(11) DEFAULT NULL,
  `tf_primary_method` varchar(64) DEFAULT NULL,
  `tf_totp_secret` varchar(255) DEFAULT NULL,
  `tf_phone_number` varchar(128) DEFAULT NULL,
  `create_datetime` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_datetime` timestamp NOT NULL DEFAULT current_timestamp(),
  `username` varchar(255) DEFAULT NULL,
  `us_totp_secrets` text DEFAULT NULL,
  `us_phone_number` varchar(128) DEFAULT NULL,
  `email_change_new` varchar(255) DEFAULT NULL,
  `email_change_code` varchar(20) DEFAULT NULL,
  `email_change_last` timestamp NULL DEFAULT NULL,
  `fs_webauthn_user_handle` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE `webauthn` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(255) UNSIGNED NOT NULL,
  `credential_id` blob NOT NULL,
  `public_key` blob NOT NULL,
  `sign_count` int(11) NOT NULL DEFAULT 0,
  `transports` text DEFAULT NULL,
  `extensions` varchar(255) DEFAULT NULL,
  `lastuse_datetime` datetime NOT NULL,
  `name` varchar(64) NOT NULL,
  `usage` varchar(64) NOT NULL,
  `backup_state` tinyint(1) NOT NULL,
  `device_type` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


ALTER TABLE `role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);


ALTER TABLE `roles_users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `role_id` (`role_id`);


ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `fs_uniquifier` (`fs_uniquifier`),
  ADD UNIQUE KEY `fs_webauthn_user_handle` (`fs_webauthn_user_handle`),
  ADD UNIQUE KEY `username` (`username`);


ALTER TABLE `webauthn`
  ADD PRIMARY KEY (`id`),
  ADD KEY `credential_id_index` (`user_id`);


ALTER TABLE `role`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;


ALTER TABLE `user`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;


ALTER TABLE `webauthn`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;


ALTER TABLE `webauthn`
  ADD CONSTRAINT `user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;
